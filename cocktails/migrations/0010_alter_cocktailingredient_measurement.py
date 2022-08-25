# Generated by Django 3.2 on 2022-08-19 14:05

import cocktails.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0009_rename_recipeingredient_cocktailingredient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktailingredient',
            name='measurement',
            field=models.CharField(
                max_length=54,
                validators=[cocktails.validators.validate_measurements]),
        ),
    ]
