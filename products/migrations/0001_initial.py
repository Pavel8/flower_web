# Generated by Django 5.1.7 on 2025-03-21 09:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('yes', 'Živé'), ('no', 'Umělé')], default='yes', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('stock_status', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('color', models.CharField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('white', 'White'), ('pink', 'Pink'), ('purple', 'Purple'), ('orange', 'Orange')], default='red', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_1', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_2', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_3', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_4', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('additional_image_5', models.ImageField(blank=True, null=True, upload_to='products/images/')),
                ('alive', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.alive')),
                ('occasion', models.ManyToManyField(to='products.occasion')),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.type')),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('idcode', models.CharField(max_length=13, unique=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
