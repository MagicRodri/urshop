# Generated by Django 4.1.1 on 2022-10-31 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_brand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='categories/thumbnails'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='categories/originals'),
        ),
    ]