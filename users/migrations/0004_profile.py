# Generated by Django 5.0.7 on 2024-08-02 20:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_newuser_password1_remove_newuser_password2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=False)),
                ('parent_phone', models.CharField(max_length=11)),
                ('state', models.CharField(max_length=150)),
                ('grade', models.CharField(max_length=250)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]