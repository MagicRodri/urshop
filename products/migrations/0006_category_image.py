# Generated by Django 4.1.1 on 2022-10-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_brand_is_active_image_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories/'),
        ),
    ]