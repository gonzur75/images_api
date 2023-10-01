# Generated by Django 4.2.5 on 2023-10-01 09:30

from django.db import migrations, models
import images.validators


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='url',
            field=models.FileField(upload_to='images/', validators=[images.validators.validate_file_type]),
        ),
    ]
