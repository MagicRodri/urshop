# Generated by Django 4.1.1 on 2022-10-03 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_brand_name_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
