# Generated by Django 3.1.6 on 2021-02-15 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0022_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercompany',
            name='laguange',
            field=models.CharField(choices=[('english', 'English'), ('spanish', 'Spanish')], default='English', max_length=15),
        ),
        migrations.AddField(
            model_name='usercompany',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
