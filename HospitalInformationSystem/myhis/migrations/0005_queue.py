# Generated by Django 4.2.4 on 2023-09-08 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myhis', '0004_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Queue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myhis.patient')),
            ],
        ),
    ]
