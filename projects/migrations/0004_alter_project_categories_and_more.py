# Generated by Django 4.0.3 on 2022-03-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_categories'),
        ('projects', '0003_project_date_project_sorting_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sorting_priority',
            field=models.SmallIntegerField(default=0, help_text='A high sorting priority causes projects to be displayed first in the index view, while a negative value places them at the end. Default is 0.'),
        ),
    ]
