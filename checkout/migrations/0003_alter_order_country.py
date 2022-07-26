'''
Imports relevant django packages
'''
from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):
    '''
    Migration dependencies for the checkout
    '''
    dependencies = [
        ('checkout', '0002_auto_20220712_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
