# Generated by Django 4.1 on 2022-09-23 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='is_selected',
            field=models.BooleanField(default=False),
        ),
    ]
