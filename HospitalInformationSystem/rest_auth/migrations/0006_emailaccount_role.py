# Generated by Django 4.2.4 on 2023-08-24 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_auth', '0005_remove_emailaccount_age_remove_emailaccount_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailaccount',
            name='role',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
