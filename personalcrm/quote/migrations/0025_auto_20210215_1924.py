# Generated by Django 3.1.6 on 2021-02-15 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0024_auto_20210215_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercompany',
            name='logo',
            field=models.ImageField(default='default-logo.png', upload_to='company_logos'),
        ),
    ]
