# Generated by Django 5.1.1 on 2024-09-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_shopentry_delete_moodentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopentry',
            name='rating',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='shopentry',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]
