# Generated by Django 4.1 on 2024-02-23 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='todo',
            new_name='title',
        ),
    ]
