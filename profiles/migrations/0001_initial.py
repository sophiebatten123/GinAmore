'''
Imports relevant django packages
'''
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):
    '''
    Migration dependencies for the profiles page
    '''
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('default_phone_number', models.CharField(
                    blank=True,
                    max_length=20,
                    null=True)),
                ('default_email', models.EmailField(
                    blank=True,
                    max_length=250,
                    null=True)),
                ('default_country', django_countries.fields.CountryField(
                    blank=True,
                    max_length=2,
                    null=True)),
                ('default_town_or_city', models.CharField(
                    blank=True,
                    max_length=50,
                    null=True)),
                ('default_postcode', models.CharField(
                    blank=True,
                    max_length=20,
                    null=True)),
                ('default_street_address1', models.CharField(
                    blank=True,
                    max_length=100,
                    null=True)),
                ('default_street_address2', models.CharField(
                    blank=True,
                    max_length=100,
                    null=True)),
                ('default_county', models.CharField(
                    blank=True,
                    max_length=100,
                    null=True)),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
