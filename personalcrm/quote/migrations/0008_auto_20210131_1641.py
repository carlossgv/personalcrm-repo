# Generated by Django 3.1.5 on 2021-01-31 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0007_auto_20210131_1508'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='quotedProducts',
            new_name='QuotedProduct',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
