from django.db import models
from datetime import datetime
from concurrency.fields import IntegerVersionField



# Create your models here.
class Teams(models.Model):
    version = IntegerVersionField()
    TeamName = models.CharField(max_length=50, null=True)
    Points = models.IntegerField(default= 0)

    def __str__(self):
        return self.TeamName


class Player(models.Model):
    Team = models.ForeignKey(Teams, on_delete=models.CASCADE, null=True)
    version = IntegerVersionField()
    PName = models.CharField(max_length=100, null=True)
    PAge = models.IntegerField(null=True)
    PType = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.PName


class Series(models.Model):
    SeriesName = models.CharField(max_length=100, null=True)
    StartDate = models.DateField(default=datetime.now, null=True)
    EndDate = models.DateField(default=datetime.now, null=True)
    Teams = models.ManyToManyField(Teams)
    version = IntegerVersionField()

    def __str__(self):
        return self.SeriesName


class Match(models.Model):
    Series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)

    Teams = models.ManyToManyField(Teams)

    MatchDate = models.DateField(null =True)
    WinningTeam = models.CharField(max_length=100,default = "NoTeam")
    version = IntegerVersionField()


