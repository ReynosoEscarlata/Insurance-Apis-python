# Generated by Django 4.2 on 2024-02-02 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0003_alter_driver_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='address',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
