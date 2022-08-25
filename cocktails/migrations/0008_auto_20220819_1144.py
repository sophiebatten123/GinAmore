# Generated by Django 3.2 on 2022-08-19 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0007_rename_category_cocktailcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cocktail',
            name='ingredients',
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('quantity', models.CharField(max_length=54)),
                ('measurement', models.CharField(max_length=54)),
                ('cocktail', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    to='cocktails.cocktail')),
            ],
        ),
    ]
