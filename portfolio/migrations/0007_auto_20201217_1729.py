# Generated by Django 3.1.4 on 2020-12-17 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20201217_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=256, null=True),
        ),
    ]
