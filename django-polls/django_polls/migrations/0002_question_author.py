# Generated by Django 5.0.3 on 2024-03-21 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.CharField(default='anonymous', max_length=200),
        ),
    ]
