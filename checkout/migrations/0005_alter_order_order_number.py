'''
Imports relevant django packages
'''
from django.db import migrations, models


class Migration(migrations.Migration):
    '''
    Migration dependencies for the checkout
    '''
    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(editable=False, max_length=32),
        ),
    ]
