# Generated by Django 5.2 on 2025-05-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veva', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.CharField(max_length=255)),
                ('user_password', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=100)),
                ('user_mobile', models.CharField(max_length=60)),
                ('registered_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User_registers',
        ),
    ]
