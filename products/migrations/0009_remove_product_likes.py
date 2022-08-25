'''
Imports relevant django packages
'''
from django.db import migrations


class Migration(migrations.Migration):
    '''
    Migrations
    '''
    dependencies = [
        ('products', '0008_remove_review_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='likes',
        ),
    ]
