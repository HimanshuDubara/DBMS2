# Generated by Django 3.0.6 on 2020-06-06 05:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='Series_id',
        ),
        migrations.RemoveField(
            model_name='player',
            name='Team_id',
        ),
        migrations.AddField(
            model_name='match',
            name='Series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Series'),
        ),
        migrations.AddField(
            model_name='player',
            name='Team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='teams.Teams'),
        ),
        migrations.AlterField(
            model_name='match',
            name='Teams',
            field=models.ManyToManyField(null=True, to='teams.Teams'),
        ),
        migrations.AlterField(
            model_name='player',
            name='PAge',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='PName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='PType',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='EndDate',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='SeriesName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='StartDate',
            field=models.DateField(default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='series',
            name='Teams',
            field=models.ManyToManyField(null=True, to='teams.Teams'),
        ),
        migrations.AlterField(
            model_name='teams',
            name='TeamName',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='teams',
            name='TeamRank',
            field=models.IntegerField(default=0, null=True),
        ),
    ]