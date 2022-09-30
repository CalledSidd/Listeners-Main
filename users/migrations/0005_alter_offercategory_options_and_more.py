# Generated by Django 4.1 on 2022-09-20 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_offerproduct_offercategory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='offercategory',
            options={'verbose_name': 'OfferCategory', 'verbose_name_plural': 'Offer Categories'},
        ),
        migrations.AlterModelOptions(
            name='offerproduct',
            options={'verbose_name': 'Offer Product', 'verbose_name_plural': 'Offer Products'},
        ),
        migrations.AddField(
            model_name='products',
            name='discount_price',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]