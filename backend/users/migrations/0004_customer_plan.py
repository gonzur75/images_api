# Generated by Django 4.2.5 on 2023-10-02 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='plan',
            field=models.IntegerField(null=True),
        ),
    ]