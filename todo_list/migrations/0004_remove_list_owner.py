# Generated by Django 3.0.7 on 2020-06-21 05:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0003_auto_20200621_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='owner',
        ),
    ]
