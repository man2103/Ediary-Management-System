# Generated by Django 4.0 on 2023-10-06 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eDiary', '0002_notes_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='file',
        ),
    ]