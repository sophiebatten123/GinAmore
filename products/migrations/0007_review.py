'''
Imports relevant django packages
'''
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    '''
    Migration dependencies for products
    '''
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0006_product_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('user_review', models.TextField(max_length=250)),
                ('product_rating', models.IntegerField(
                    choices=[(5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')],
                    default=5)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='products.product')),
                ('user', models.ForeignKey(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
