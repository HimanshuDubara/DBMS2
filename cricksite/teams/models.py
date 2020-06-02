from django.db import models
from datetime import datetime
from django.urls import reverse
from concurrency.fields import IntegerVersionField
from django.http import Http404


# Create your models here.
class Teams(models.Model):
    TeamID = models.IntegerField(primary_key=True)
    TeamName = models.CharField(max_length=50)
    TeamRank = models.IntegerField()

    def __str__(self):
        return self.TeamName


class Player(models.Model):
    TeamID = models.ForeignKey(Teams, on_delete=models.CASCADE)
    PID = models.IntegerField(primary_key=True)
    PName = models.CharField(max_length=100)
    PAge = models.IntegerField()
    PType = models.CharField(max_length=150)

    def __str__(self):
        return self.PName


class Series(models.Model):
    SeriesName = models.CharField(max_length=100)
    StartDate = models.DateField(default=datetime.now, blank=True)
    EndDate = models.DateField(default=datetime.now, blank=True)
    Teams = models.ManyToManyField(Teams)

    def __str__(self):
        return self.SeriesName


class Match(models.Model):
    Series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
    MatchID = models.IntegerField(primary_key=True)
    Teams = models.ManyToManyField(Teams)

    def __str__(self):
        return self.MatchID
