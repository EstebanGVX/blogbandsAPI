# Generated by Django 4.1.7 on 2023-05-01 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bands', '0004_alter_categories_options_alter_members_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categories',
            options={'ordering': ['name_categorie']},
        ),
        migrations.RenameField(
            model_name='categories',
            old_name='name',
            new_name='name_categorie',
        ),
    ]
