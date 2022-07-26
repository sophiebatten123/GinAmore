'''
Imports relevant django packages
'''
from django.db import migrations


class Migration(migrations.Migration):
    '''
    Migration dependencies for products
    '''
    dependencies = [
        ('products', '0007_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product_rating',
        ),
    ]
