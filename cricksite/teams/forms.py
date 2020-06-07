from django import forms
from .models import Teams, Series, Match, Player
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class teamsform(forms.Form):
    TeamName = forms.CharField(label="Team Name")


class playerform(forms.Form):
    PName = forms.CharField(label="Player Name")
    PAge = forms.IntegerField(label="Player Age")
    PType = forms.CharField(label="Player Type")
    Team = forms.ModelChoiceField(queryset=Teams.objects.all(), label="Team")


class seriesform(forms.Form):
    SeriesName = forms.CharField(label="Series Name")
    StartDate = forms.DateField(label="Start Date")
    EndDate = forms.DateField(label="End Date")
    Teams = forms.ModelMultipleChoiceField(queryset=Teams.objects.all())

    def clean_EndDate(self):
        data = self.cleaned_data['EndDate']
        data1 = self.cleaned_data['StartDate']
        if data < data1:
            raise ValidationError(_("End Date cannot be before Start Date"))
        return data


class matchform(forms.Form):
    Series = forms.ModelChoiceField(queryset=Series.objects.all(), label="Series")
    Teams = forms.ModelMultipleChoiceField(queryset=Teams.objects.all())
    MatchDate = forms.DateField(label="Match Date")


class searchform(forms.Form):
    a = ((1, 'All'), (2, 'Teams'), (3, 'Players'), (4, 'Series'))
    searchvalue = forms.CharField(label="Search Value")
    type1 = forms.ChoiceField(choices=a)


class match_result_form(forms.Form):

    def __init__(self, teamslist, *args, **kwargs):
        super(match_result_form, self).__init__(*args, **kwargs)
        self.fields['Team_Name'] = forms.ChoiceField(choices=tuple([(t.TeamName, t.TeamName) for t in teamslist]))
