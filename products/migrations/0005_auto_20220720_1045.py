'''
Imports relevant django packages
'''
from django.db import migrations, models


class Migration(migrations.Migration):
    '''
    Migration dependencies for products
    '''
    dependencies = [
        ('products', '0004_auto_20220714_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(blank=True, max_length=2000, null=True),
        ),
    ]
