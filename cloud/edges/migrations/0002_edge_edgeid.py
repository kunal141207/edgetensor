# Generated by Django 2.2.11 on 2020-03-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edges', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='edge',
            name='edgeid',
            field=models.FloatField(default=0),
        ),
    ]
