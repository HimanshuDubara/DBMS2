# Generated by Django 3.0.6 on 2020-06-02 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_match_series'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mteams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='STeams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
