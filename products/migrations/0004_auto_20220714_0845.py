'''
Imports relevant django packages
'''
from django.db import migrations, models


class Migration(migrations.Migration):
    '''
    Migration dependencies for products
    '''
    dependencies = [
        ('products', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.URLField(max_length=2000),
        ),
    ]
