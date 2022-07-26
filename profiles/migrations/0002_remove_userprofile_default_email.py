'''
Imports relevant django packages
'''
from django.db import migrations


class Migration(migrations.Migration):
    '''
    Migration dependecies for the profiles
    '''
    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='default_email',
        ),
    ]
