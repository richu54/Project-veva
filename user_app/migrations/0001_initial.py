# Generated by Django 5.2 on 2025-05-08 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='additional_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_address', models.CharField(blank=True, max_length=255, null=True)),
                ('user_state', models.CharField(blank=True, max_length=100, null=True)),
                ('user_pincode', models.CharField(blank=True, max_length=20, null=True)),
                ('user_dob', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
