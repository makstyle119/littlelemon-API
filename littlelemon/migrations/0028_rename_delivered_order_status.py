# Generated by Django 4.1.6 on 2023-02-10 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemon', '0027_remove_purchase_orderitems_purchaseitem_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='delivered',
            new_name='status',
        ),
    ]
