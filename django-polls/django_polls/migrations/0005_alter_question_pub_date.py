# Generated by Django 5.0.3 on 2024-03-22 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_choice_choice_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 22, 7, 54, 53, 732936, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
