# Generated by Django 3.1.5 on 2021-02-04 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0013_auto_20210204_1849'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='id_number',
            new_name='legal_id',
        ),
    ]