# Generated by Django 3.1.5 on 2021-02-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0010_auto_20210201_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='quotedproduct',
            name='discount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
