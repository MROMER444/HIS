# Generated by Django 4.2.4 on 2023-08-23 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhis', '0003_alter_patient_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.FileField(default=None, upload_to='patient_images'),
            preserve_default=False,
        ),
    ]
