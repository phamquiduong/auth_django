# Generated by Django 5.1.7 on 2025-03-16 11:44

import django.utils.timezone
from django.db import migrations, models

import _user.constants.role


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('role', models.CharField(default=_user.constants.role.Roles['GUEST'], max_length=10)),
                ('first_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(blank=True, max_length=150, null=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
