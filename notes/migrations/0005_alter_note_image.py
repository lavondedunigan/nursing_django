# Generated by Django 5.2.1 on 2025-06-11 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
