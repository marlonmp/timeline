# Generated by Django 4.1.5 on 2023-01-24 02:58

import apps.user.models
from django.db import migrations, models
import uuid


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
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('username', models.CharField(editable=False, max_length=150, unique=True)),
                ('nickname', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(choices=[('UF', 'Unverified'), ('AC', 'Active'), ('DS', 'Disabled'), ('DL', 'Deleted')], default='UF', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', apps.user.models.Manager()),
            ],
        ),
    ]