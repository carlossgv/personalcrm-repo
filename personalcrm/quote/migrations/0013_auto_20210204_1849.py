# Generated by Django 3.1.5 on 2021-02-04 18:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0012_usercompany'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercompany',
            old_name='company',
            new_name='name',
        ),
    ]
