# Generated by Django 3.0.7 on 2020-06-21 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0002_list_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='user',
            new_name='owner',
        ),
    ]