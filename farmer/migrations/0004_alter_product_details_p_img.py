# Generated by Django 4.1.4 on 2023-03-14 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0003_rename_farmer_order_order_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_details',
            name='p_img',
            field=models.ImageField(upload_to='media'),
        ),
    ]
