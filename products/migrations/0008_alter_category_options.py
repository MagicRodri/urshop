# Generated by Django 4.1.1 on 2022-10-28 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_category_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
