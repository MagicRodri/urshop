# Generated by Django 4.1.1 on 2023-01-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_stripepayment_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripepayment',
            name='intent_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stripepayment',
            name='stripe_charge_id',
            field=models.CharField(max_length=100),
        ),
    ]