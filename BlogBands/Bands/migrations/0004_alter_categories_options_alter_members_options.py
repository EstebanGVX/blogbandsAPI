# Generated by Django 4.1.7 on 2023-04-29 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bands', '0003_alter_bands_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='members',
            options={'ordering': ['firstname']},
        ),
    ]
