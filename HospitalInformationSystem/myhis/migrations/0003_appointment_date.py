# Generated by Django 4.2.4 on 2023-09-01 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhis', '0002_remove_appointment_appointment_datetime_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
