'''
Imports relevant django packages
'''
from django.shortcuts import render, reverse, redirect, get_object_or_404
from .models import (
    Cocktail,
    CocktailReview,
    CocktailCategory,
    CocktailIngredient,
    CocktailRecipeStep
)
from .forms import (
    CocktailForm,
    CocktailReviewForm,
    CocktailIngredientForm,
    CocktailStepForm,
    CocktailIngredientFormSet,
    StepsIngredientFormSet
    )
from django.forms.models import modelformset_factory
from django.contrib import messages


def cocktails(request):
    '''
    A view to return the render all cocktail recipes
    '''
    cocktail_items = Cocktail.objects.all()
    categories = None

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        cocktail_items = cocktail_items.filter(category__name__in=categories)
        categories = CocktailCategory.objects.filter(name__in=categories)

    context = {
        'cocktail_items': cocktail_items,
        'current_categories': categories,
    }

    return render(request, 'cocktails/cocktails.html', context)


def cocktail_detail(request, product_id):
    '''
    A view to return the cocktails recipe information
    '''
    cocktail = get_object_or_404(Cocktail, pk=product_id)
    ingredients = cocktail.cocktail_ingredients_list.all()
    recipe = cocktail.cocktail_steps_list.all()

    if request.method == 'POST':

        review_form = CocktailReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():

            review_form.instance.user = request.user
            cocktail_review = review_form.save(commit=False)
            cocktail_review.cocktail = cocktail
            cocktail_review.save()
            messages.success(request, ('Thank you for your review!'))

            return redirect(reverse('cocktail_detail', args=[cocktail.id]))
        else:
            messages.error(
                request,
                'Please login to create a review on one of our cocktails!')
            return redirect(reverse('cocktail_detail', args={cocktail.id}))
    else:
        review_form = CocktailReviewForm()

    cocktail_reviews = CocktailReview.objects.filter(cocktail=cocktail)

    context = {
        'cocktail': cocktail,
        'cocktail_reviews': cocktail_reviews,
        'review_form': review_form,
        'ingredients': ingredients,
        'recipe': recipe,
    }

    return render(request, 'cocktails/cocktail_detail.html', context)


def add_cocktail(request):
    '''
    Add a cocktail to the site
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can add cocktails')
        return redirect(reverse('home'))

    if request.method == 'POST':
        cocktailingredientformset = modelformset_factory(
            CocktailIngredient,
            form=CocktailIngredientForm,
            extra=0
            )
        stepsingredientformset = modelformset_factory(
            CocktailRecipeStep,
            form=CocktailStepForm,
            extra=0
            )
        formset = cocktailingredientformset(
            request.POST,
            queryset=[],
            prefix="form1"
            )
        formset_2 = stepsingredientformset(
            request.POST,
            queryset=[],
            prefix="form2"
            )
        form = CocktailForm(request.POST, request.FILES)
        if all([form.is_valid(), formset.is_valid(), formset_2.is_valid()]):
            parent = form.save(commit=False)
            parent.save()
            for form in formset:
                for form_2 in formset_2:
                    child = form.save(commit=False)
                    child_2 = form_2.save(commit=False)
                    child.cocktail = parent
                    child_2.cocktail = parent
                    child.save()
                    child_2.save()
            messages.success(request, 'Successfully added a cocktail!')
            return redirect(reverse('add_cocktail'))
        else:
            messages.error(
                request,
                'Failed to add the cocktail. Ensure the form is valid'
                )
    else:
        form = CocktailForm()
        formset = CocktailIngredientFormSet(prefix="form1")
        formset_2 = StepsIngredientFormSet(prefix="form2")

    template = 'cocktails/add_cocktail.html'
    context = {
        'form': form,
        'formset': formset,
        'formset_2': formset_2,
    }

    return render(request, template, context)


def edit_cocktail(request, product_id):
    '''
    Edit a cocktail from the store
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can edit cocktails')
        return redirect(reverse('home'))

    cocktail = get_object_or_404(Cocktail, pk=product_id)
    ingredients = cocktail.cocktail_ingredients_list.all()
    recipe = cocktail.cocktail_steps_list.all()

    if request.method == 'POST':
        cocktailingredientformset = modelformset_factory(
            CocktailIngredient,
            form=CocktailIngredientForm,
            extra=0
            )
        stepsingredientformset = modelformset_factory(
            CocktailRecipeStep,
            form=CocktailStepForm,
            extra=0
            )
        ingredients = cocktail.cocktail_ingredients_list.all()
        recipe = cocktail.cocktail_steps_list.all()
        formset = cocktailingredientformset(
            request.POST,
            ingredients,
            prefix="form1"
            )
        formset_2 = stepsingredientformset(
            request.POST,
            recipe,
            prefix="form2"
            )
        form = CocktailForm(request.POST, request.FILES, instance=cocktail)
        if all([form.is_valid(), formset.is_valid(), formset_2.is_valid()]):
            parent = form.save(commit=False)
            parent.save()
            for form in formset:
                for form_2 in formset_2:
                    child = form.save(commit=False)
                    child_2 = form_2.save(commit=False)
                    child.cocktail = parent
                    child_2.cocktail = parent
                    child.save()
                    child_2.save()
            messages.success(request, 'Successfully updated the cocktail!')
            return redirect(reverse('cocktail_detail', args=[cocktail.id]))
        else:
            messages.error(
                request,
                'Failed to edit the cocktail. Ensure the form is valid'
                )
    else:
        form = CocktailForm(instance=cocktail)
        cocktailingredientformset = modelformset_factory(
            CocktailIngredient,
            CocktailIngredientForm,
            extra=0)
        stepsingredientformset = modelformset_factory(
            CocktailRecipeStep,
            form=CocktailStepForm,
            extra=0
            )
        formset_2 = stepsingredientformset(queryset=recipe, prefix="form2")
        formset = cocktailingredientformset(
            queryset=ingredients,
            prefix="form1"
            )
        messages.info(request, f'You are editing {cocktail.name}')

    template = 'cocktails/edit_cocktail.html'
    context = {
        'form': form,
        'formset': formset,
        'formset_2': formset_2,
        'cocktail': cocktail,
    }

    return render(request, template, context)


def delete_cocktail(request, product_id):
    '''
    Deletes the product from the shop
    '''
    if not request.user.is_superuser:
        messages.error(
            request,
            'Sorry, only store owners can delete cocktails'
            )
        return redirect(reverse('home'))

    cocktail = get_object_or_404(Cocktail, pk=product_id)
    cocktail.delete()
    messages.success(request, 'Cocktail has been deleted!')

    return redirect(reverse('cocktails'))


def delete_cocktail_review(request, review_id):
    '''
    Deletes the review from the product
    '''
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can delete reviews!')
        return redirect(reverse('home'))

    review = get_object_or_404(CocktailReview, pk=review_id)
    review.delete()
    messages.success(request, 'Review has been deleted!')

    return redirect(reverse('cocktails'))
