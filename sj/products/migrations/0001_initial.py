# Generated by Django 5.0.3 on 2024-05-03 20:38

import common.utils
import django.db.models.deletion
import parler.fields
import parler.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SuperCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(default=32000, verbose_name='order')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_present', models.BooleanField(default=False, verbose_name='presence')),
                ('actual_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='actual_price')),
                ('current_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='current_price')),
                ('order', models.PositiveSmallIntegerField(default=32000, verbose_name='order')),
                ('code', models.CharField(blank=True, max_length=20, null=True, unique=True, verbose_name='part_number')),
            ],
            options={
                'abstract': False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('supercategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.supercategory')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=('products.supercategory',),
        ),
        migrations.CreateModel(
            name='ProductImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to=common.utils.upload_product_img_to, verbose_name='product_img')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='img_urls', to='products.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'product_img',
                'verbose_name_plural': 'product_imgs',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('supercategory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.supercategory')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.supercategory', verbose_name='parent_category')),
            ],
            options={
                'verbose_name': 'subcategory',
                'verbose_name_plural': 'subcategories',
            },
            bases=('products.supercategory',),
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='products.subcategory'),
        ),
        migrations.CreateModel(
            name='ProductTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='product_name')),
                ('slug', models.SlugField(max_length=130, unique=True, verbose_name='url')),
                ('description', models.TextField(verbose_name='product_type')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='products.product')),
            ],
            options={
                'verbose_name': 'product Translation',
                'db_table': 'products_product_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='SuperCategoryTranslation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(max_length=40, unique=True, verbose_name='category_name')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('master', parler.fields.TranslationsForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='products.supercategory')),
            ],
            options={
                'verbose_name': 'super category Translation',
                'db_table': 'products_supercategory_translation',
                'db_tablespace': '',
                'managed': True,
                'default_permissions': (),
                'unique_together': {('language_code', 'master')},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
