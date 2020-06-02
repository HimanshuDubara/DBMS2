from django.db import models
from django.urls import reverse
from concurrency.fields import IntegerVersionField
from django.http import Http404


# Create your models here.
class Teams(models.Model):
    TeamID = models.IntegerField(primary_key=True)
    TeamName = models.CharField(max_length=50)
    TeamRank = models.IntegerField()
    version = IntegerVersionField()

    def __str__(self):
        return self.TeamName


class Player(models.Model):
    TeamID = models.ForeignKey(Teams, on_delete=models.CASCADE)
    PID = models.IntegerField(primary_key=True)
    PName = models.CharField(max_length=100)
    PAge = models.IntegerField()
    PType = models.CharField(max_length=150)
    version = IntegerVersionField()

    def __str__(self):
        return self.PName


class Series(models.Model):
    SeriesID: models.IntegerField(primary_key=True)
    SeriesName: models.CharField(max_length=100)
    StartDate: models.DateField()
    EndDate: models.DateField()
    Teams: models.ManyToManyField(Teams)
    version = IntegerVersionField()

    def __str__(self):
        return self.SeriesID


class Match(models.Model):
    SeriesID: models.ForeignKey(Series, on_delete=models.CASCADE)
    MatchID: models.IntegerField(primary_key=True)
    Teams: models.ManyToManyField(Teams)
    version = IntegerVersionField()

    def __str__(self):
        return self.MatchID
