# Generated by Django 4.2.10 on 2024-04-25 14:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0004_remove_product_rating_productrating'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductRating',
            new_name='Star',
        ),
    ]
