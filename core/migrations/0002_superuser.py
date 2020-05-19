from __future__ import unicode_literals
from django.db import migrations
from django.contrib.auth import get_user_model


def forwards_func(apps, schema_editor):
    User = get_user_model()
    superuser = User.objects.filter(username='pmcarlos')
    if not superuser.exists():
        User.objects.create_superuser('pmcarlos', email='pmcarlosdev@gmail.com', password='123456')


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [('core', '0001_initial')]
    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
