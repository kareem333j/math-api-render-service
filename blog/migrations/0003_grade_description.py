# Generated by Django 5.0.7 on 2024-09-22 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_course_grade'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]