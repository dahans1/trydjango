# Generated by Django 5.0.6 on 2024-06-15 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_featured"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="summary",
            field=models.TextField(blank=True),
        ),
    ]
