# Generated by Django 5.2 on 2025-06-22 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_wishlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping_address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=120)),
                ('mobile', models.CharField(max_length=15)),
                ('pincode', models.CharField(max_length=10)),
                ('locality', models.CharField(max_length=150)),
                ('address_line', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('KL', 'Kerala'), ('KA', 'Karnataka'), ('TN', 'Tamil Nadu')], max_length=2)),
                ('landmark', models.CharField(blank=True, max_length=150)),
                ('alt_phone', models.CharField(blank=True, max_length=15)),
            ],
        ),
    ]
