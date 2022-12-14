# Generated by Django 4.1.1 on 2022-10-10 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('address_type', models.CharField(choices=[('BILLING', 'Billing address'), ('SHIPPING', 'Shipping address')], max_length=16)),
                ('address_line_1', models.CharField(max_length=128)),
                ('address_line_2', models.CharField(blank=True, max_length=128)),
                ('country', models.CharField(max_length=128)),
                ('state', models.CharField(max_length=128)),
                ('city', models.CharField(max_length=128)),
                ('postal_code', models.CharField(max_length=128)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
    ]
