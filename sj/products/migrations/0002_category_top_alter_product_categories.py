# Generated by Django 5.0.3 on 2024-05-03 20:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='top',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.supercategory'),
        ),
    ]
