# Generated by Django 4.1.4 on 2023-03-13 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0002_customer_details_c_id_farmer_details_f_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='farmer_order',
            new_name='order_details',
        ),
    ]
