# Generated by Django 4.1.1 on 2022-10-28 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
    ]