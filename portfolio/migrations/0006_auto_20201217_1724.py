# Generated by Django 3.1.4 on 2020-12-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_job_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Registration Open', 'Registration Open'), ('Registration Closed', 'Registration Closed'), ('Event Completed', 'Event Completed')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='status',
            field=models.CharField(choices=[('Accepting CVs', 'Accepting CVs'), ('Interviewing', 'Interviewing'), ('Vacancy Filled', 'Vacancy Filled')], max_length=30, null=True),
        ),
    ]
