# Generated by Django 4.0.3 on 2022-03-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_semester_course_year_alter_course_units'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='course',
            name='in_progress',
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.IntegerField(choices=[(1, 'Planned'), (2, 'In Progress'), (3, 'Completed')], default=1),
        ),
    ]
