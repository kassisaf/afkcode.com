# Generated by Django 4.0.3 on 2022-03-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_categories'),
        ('courses', '0004_remove_course_completed_remove_course_in_progress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.category'),
        ),
    ]
