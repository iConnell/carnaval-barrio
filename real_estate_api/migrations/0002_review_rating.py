# Generated by Django 4.1.7 on 2023-03-07 19:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]