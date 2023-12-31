# Generated by Django 4.2.5 on 2023-10-06 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExpiringLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('token', models.UUIDField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('duration', models.IntegerField()),
            ],
        ),
    ]
