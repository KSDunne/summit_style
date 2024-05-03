# Generated by Django 4.2.10 on 2024-05-03 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0007_alter_star_body_alter_star_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, related_name='product_wishlist', to=settings.AUTH_USER_MODEL),
        ),
    ]