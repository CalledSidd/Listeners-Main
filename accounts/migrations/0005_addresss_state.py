# Generated by Django 4.1 on 2022-08-25 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_rename_address_addresss'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresss',
            name='state',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
