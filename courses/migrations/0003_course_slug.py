# Generated by Django 4.0.2 on 2022-02-13 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_school_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=25),
        ),
    ]