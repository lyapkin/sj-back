# Generated by Django 5.0.3 on 2024-05-09 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_favorite_brands_favoriteproduct_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoriteproduct',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
