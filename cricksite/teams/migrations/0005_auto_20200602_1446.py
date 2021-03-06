# Generated by Django 3.0.6 on 2020-06-02 09:16

import concurrency.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_auto_20200602_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='version',
            field=concurrency.fields.IntegerVersionField(default=0, help_text='record revision number'),
        ),
        migrations.AddField(
            model_name='player',
            name='version',
            field=concurrency.fields.IntegerVersionField(default=0, help_text='record revision number'),
        ),
        migrations.AddField(
            model_name='series',
            name='version',
            field=concurrency.fields.IntegerVersionField(default=0, help_text='record revision number'),
        ),
        migrations.AddField(
            model_name='teams',
            name='version',
            field=concurrency.fields.IntegerVersionField(default=0, help_text='record revision number'),
        ),
    ]
