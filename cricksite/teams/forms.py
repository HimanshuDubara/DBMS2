from django import forms
from .models import Teams, Player, Series, Match


class TeamForm(forms.ModelForm):
    class Meta:
        model = Teams
        fields = [
            'TeamID',
            'TeamName',
            'TeamRank'
        ]


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'TeamID',
            'PID',
            'PName',
            'PAge',
            'PType',

        ]


class SeriesForm(forms.ModelForm):
    SeriesID = forms.IntegerField()
    SeriesName = forms.CharField()
    StartDate = forms.DateField()
    EndDate = forms.DateField()
    Teams = forms.ModelMultipleChoiceField(queryset=Teams.objects.all())

    class Meta:
        model = Series
        fields = [
             'SeriesID',
             'SeriesName',
             'StartDate',
             'EndDate',
             'Teams'
         ]


class MatchForm(forms.ModelForm):
    SeriesID = forms.ModelChoiceField(queryset=Series.objects.all())
    MatchID = forms.IntegerField()
    Teams = forms.ModelMultipleChoiceField(queryset=Teams.objects.all())

    class Meta:
        model = Match
        fields = [
            'SeriesID',
            'MatchID',
            'Teams'
        ]

