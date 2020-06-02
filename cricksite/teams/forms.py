from django import forms
from .models import Teams, Player, Series, Match


class TeamForm(forms.ModelForm):
    version = forms.IntegerField(required=False)

    class Meta:
        model = Teams
        fields = [
            'TeamID',
            'TeamName',
            'TeamRank'
        ]

    def savemt(self, *args, **kwargs):
        if self.version != Teams.objects.get(TeamID=self.pk).version:
            raise Http404('Ooops!!!! Concurrency Issues, Try Again')
        super(Teams, self).save(*args, **kwargs)


class PlayerForm(forms.ModelForm):
    version = forms.IntegerField(required=False)

    class Meta:
        model = Player
        fields = [
            'TeamID',
            'PID',
            'PName',
            'PAge',
            'PType',

        ]


    def savemp(self, *args, **kwargs):
        if self.version != Player.objects.get(PID=self.pk).version:
            raise Http404('Ooops!!!! Concurrency Issues, Try Again')
        super(Player, self).save(*args, **kwargs)


class SeriesForm(forms.ModelForm):
    SeriesID = forms.IntegerField()
    SeriesName = forms.CharField()
    StartDate = forms.DateField()
    EndDate = forms.DateField()
    Teams = forms.ModelMultipleChoiceField(queryset=Teams.objects.all())
    version = forms.IntegerField(required=False)

    class Meta:
        model = Series
        fields = [
            'SeriesID',
            'SeriesName',
            'StartDate',
            'EndDate',
            'Teams'
        ]


    def savems(self, *args, **kwargs):
        if self.version != Series.objects.get(SeriesID=self.pk).version:
            raise Http404('Ooops!!!! Concurrency Issues, Try Again')
        super(Series, self).save(*args, **kwargs)


class MatchForm(forms.ModelForm):
    SeriesID = forms.ModelChoiceField(queryset=Series.objects.all())
    MatchID = forms.IntegerField()
    Teams = forms.ModelMultipleChoiceField(queryset=Teams.objects.all())
    version = forms.IntegerField(required=False)

    class Meta:
        model = Match
        fields = [
            'SeriesID',
            'MatchID',
            'Teams'
        ]


    def savemm(self, *args, **kwargs):
        if self.version != Match.objects.get(MatchID=self.pk).version:
            raise Http404('Ooops!!!! Concurrency Issues, Try Again')
