# Generated by Django 3.1.6 on 2021-02-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0021_auto_20210206_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
