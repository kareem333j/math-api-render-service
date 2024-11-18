# Generated by Django 5.0.7 on 2024-08-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='password1',
            field=models.CharField(max_length=200, null=True, verbose_name='password1'),
        ),
        migrations.AddField(
            model_name='newuser',
            name='password2',
            field=models.CharField(max_length=200, null=True, verbose_name='password2'),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='phone',
            field=models.CharField(max_length=11, unique=True, verbose_name='phone number'),
        ),
    ]
