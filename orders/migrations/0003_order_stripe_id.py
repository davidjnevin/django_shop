# Generated by Django 4.1.2 on 2022-10-08 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0002_rename_qualtity_orderitem_quantity"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="stripe_id",
            field=models.CharField(blank=True, max_length=250),
        ),
    ]