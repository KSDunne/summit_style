# Generated by Django 4.2.10 on 2024-05-20 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_wishlist'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='star',
            options={'ordering': ['-created_on']},
        ),
    ]
