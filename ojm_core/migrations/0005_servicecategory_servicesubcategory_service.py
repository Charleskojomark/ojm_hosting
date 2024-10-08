# Generated by Django 5.0.6 on 2024-06-28 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ojm_core', '0004_quote'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.TextField()),
                ('image', models.ImageField(upload_to='category_images/')),
            ],
            options={
                'verbose_name': 'Service Category',
                'verbose_name_plural': 'Service Categories',
            },
        ),
        migrations.CreateModel(
            name='ServiceSubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('short_description', models.TextField()),
                ('image', models.ImageField(upload_to='subcategory_images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='ojm_core.servicecategory')),
            ],
            options={
                'verbose_name': 'Service Subcategory',
                'verbose_name_plural': 'Service Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('original_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('recommended', models.BooleanField(default=False)),
                ('popular', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='service_images/')),
                ('cover_image', models.ImageField(upload_to='cover_images/')),
                ('need_the_service', models.TextField()),
                ('whats_included', models.TextField()),
                ('whats_excluded', models.TextField()),
                ('note_to_customer', models.TextField()),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='ojm_core.servicesubcategory')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
            },
        ),
    ]
