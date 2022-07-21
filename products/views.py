from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm


def all_products(request):
    '''
    A view to display all products
    '''

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'You didnt type anything.')
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}_{categories}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


@login_required
def product_detail(request, product_id):
    '''
    A view to return the products details
    '''
    product = get_object_or_404(Product, pk=product_id)

    liked = False
    if product.likes.filter(id=request.user.id).exists():
        liked = True

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():

            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(request, ('Thank you for your review!'))

            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()
    
    reviews = Review.objects.filter(product=product)

    context = {
        'product': product,
        'liked': liked,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    '''
    Add a product as admin to the store
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add products')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added the product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add the product. Please check the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    '''
    Edit a product found in store
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update the product. Please check your form is valid!')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    '''
    Deletes the product from the shop
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can delete products')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product has been deleted!')
    
    return redirect(reverse('products'))
