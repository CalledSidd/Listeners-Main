# Generated by Django 4.1 on 2022-08-11 04:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='Phone_number',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='account',
            name='referel_activated',
        ),
        migrations.RemoveField(
            model_name='account',
            name='referel_code',
        ),
    ]