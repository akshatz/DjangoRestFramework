# Generated by Django 3.0.8 on 2020-07-09 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='File',
            new_name='Image',
        ),
    ]
