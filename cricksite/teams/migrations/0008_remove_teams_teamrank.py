# Generated by Django 3.0.6 on 2020-06-07 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20200607_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teams',
            name='TeamRank',
        ),
    ]
