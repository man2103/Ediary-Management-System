# Generated by Django 4.0 on 2023-10-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eDiary', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='file',
            field=models.FileField(default=False, upload_to=''),
        ),
    ]