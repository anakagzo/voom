# Generated by Django 4.2.7 on 2023-11-30 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('access_type', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('access_type', models.CharField(max_length=10)),
                ('car_model', models.CharField(max_length=30)),
                ('car_plateNo', models.CharField(max_length=15)),
                ('car_BodyColor', models.CharField(max_length=15)),
                ('price_rate', models.CharField(max_length=10)),
                ('rating', models.IntegerField(blank=True, max_length=5, null=True)),
                ('reviews', models.TextField(blank=True)),
                ('order_id', models.CharField(default='None', max_length=25)),
                ('location', models.CharField(max_length=25)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_name', models.CharField(max_length=50)),
                ('seller_name', models.CharField(max_length=50)),
                ('price_rate', models.CharField(max_length=10)),
                ('delivery_fee', models.IntegerField(max_length=10)),
                ('total_amount', models.IntegerField(max_length=10)),
                ('origin', models.CharField(max_length=25)),
                ('destination', models.CharField(max_length=25)),
                ('time_engagement', models.CharField(max_length=30)),
                ('comment', models.TextField(blank=True)),
            ],
        ),
    ]