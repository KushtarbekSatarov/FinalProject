# Generated by Django 5.0.6 on 2024-05-09 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_auction', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CarMarka',
            new_name='CarMake',
        ),
    ]