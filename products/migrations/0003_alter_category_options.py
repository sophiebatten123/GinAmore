'''
Imports relevant django packages
'''
from django.db import migrations


class Migration(migrations.Migration):
    '''
    Migration dependencies for products
    '''
    dependencies = [
        ('products', '0002_auto_20220622_1333'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
