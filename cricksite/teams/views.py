from django.shortcuts import get_object_or_404, redirect, render
from .models import Teams, Player, Series, Match
from django.http import Http404
from .forms import TeamForm, PlayerForm, SeriesForm, MatchForm


# Create your views here.
def index(request):
    context = {'all_teams': Teams.objects.all().order_by('TeamRank')}
    return render(request, 'teams/index.html', context)


def details(request, teamID):
    try:
        team: object = Teams.objects.get(pk=teamID)
    except Teams.DoesNotExist:
        raise Http404("Team is not registered")
    return render(request, 'teams/details.html', {'team': team})


def players(request, teamID):
    try:
        pl: object = Player.objects.filter(TeamID_id=teamID).order_by('PID')
    except Player.DoesNotExist:
        raise Http404("No Registered Players in the Team")
    return render(request, 'teams/retplayers.html', {'pl': pl})


def search(request):
    return render(request, 'teams/search.html', {})


def searchresult(request, searchvalue, type):
    context = {
        't': Teams.objects.all().filter(TeamName__contains=searchvalue),
        'p': Player.objects.all().filter(PName__contains=searchvalue),
        's': Series.objects.all().filter(SeriesName__contains=searchvalue),
        'type': type
    }
    return render(request, 'teams/search_result.html', context)


def TeamCreate(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'teams/teams_create.html', context)


def series_index(request):
    context = {'all_series': Series.objects.all().order_by('SeriesID')}
    return render(request, 'teams/series_index.html', context)


def series_details(request, seriesID):
    try:
        ser: object = Series.objects.get(pk=seriesID)
    except Series.DoesNotExist:
        raise Http404("Series is not registered")
    return render(request, 'teams/series_details.html', {'ser': ser})


def matches(request, seriesID):
    try:
        ml: object = Match.objects.filter(SeriesID_id=seriesID).order_by('MatchID')
    except Series.DoesNotExist:
        raise Http404("No Registered Matches in the Series")
    return render(request, 'teams/retmatches.html', {'ml': ml})


def SeriesCreate(request):
    form = SeriesForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'teams/series_create.html', context)


def SeriesUpdate(request, pk1):
    a = get_object_or_404(Series, SeriesID=pk1)
    form = SeriesForm(request.POST or None, instance=a)
    if form.is_valid():
        form.savems()
        form = SeriesForm()
    context = {
        'form': form
    }
    return render(request, 'teams/series_create.html', context)


def seriesdelete(request, seriesID):
    try:
        t: object = Series.objects.get(SeriesID=seriesID)
    except Series.DoesNotExist:
        raise Http404("Please Select a valid Series to remove")
    deleted = t.delete()
    if deleted:
        return render(request, 'teams/delete_series_confirm.html', )
    else:
        raise Http404(" Sorry, we could not delete the given Series")


def MatchCreate(request):
    form = MatchForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'teams/series_create.html', context)


def MatchUpdate(request, pk1):
    a = get_object_or_404(Match, MatchID=pk1)
    form = MatchForm(request.POST or None, instance=a)
    if form.is_valid():
        form.savemm()
        form = MatchForm()
    context = {
        'form': form
    }
    return render(request, 'teams/series_create.html', context)


def matchdelete(request, matchID):
    try:
        t: object = Match.objects.get(MatchID=matchID)
    except Match.DoesNotExist:
        raise Http404("Please Select a valid match to remove")
    deleted = t.delete()
    if deleted:
        return render(request, 'teams/match_confirm_delete.html', )
    else:
        raise Http404(" Sorry, we could not delete the given match")


def TeamUpdate(request, pk1):
    a = get_object_or_404(Teams, TeamID=pk1)
    form = TeamForm(request.POST or None, instance=a)
    if form.is_valid():
        form.savemt()
        form = TeamForm()
    context = {
        'form': form
    }
    return render(request, 'teams/teams_create.html', context)


def teamdelete(request, teamID):
    try:
        t: object = Teams.objects.get(TeamID=teamID)
    except Player.DoesNotExist:
        raise Http404("Please Select a valid team to remove")
    deleted = t.delete()
    if deleted:
        return render(request, 'series1/delete_team__confirm.html', )
    else:
        raise Http404(" Sorry, we could not delete the given team")


def PlayerCreate(request):
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'teams/teams_create.html', context)


def PlayerUpdate(request, pk1):
    a = get_object_or_404(Player, PID=pk1)
    form = PlayerForm(request.POST or None, instance=a)
    if form.is_valid():
        form.savemp()
        form = TeamForm()
    context = {
        'form': form
    }
    return render(request, 'teams/teams_create.html', context)


def playerdelete(request, pid):
    try:
        t: object = Player.objects.get(PID=pid)
    except Player.DoesNotExist:
        raise Http404("Please Select a valid player to remove")
    deleted = t.delete()
    if deleted:
        return render(request, 'series1/match_confirm_delete.html', )
    else:
        raise Http404(" Sorry, we could not delete the given team")


def savems(self, *args, **kwargs):
    if self.version != Series.objects.get(SeriesID=self.pk).version:
        raise Http404('Ooops!!!! Concurrency Issues, Try Again')
    super(Series, self).save(*args, **kwargs)


def savemm(self, *args, **kwargs):
    if self.version != Match.objects.get(MatchID=self.pk).version:
        raise Http404('Ooops!!!! Concurrency Issues, Try Again')
    super(Match, self).save(*args, **kwargs)


def savemp(self, *args, **kwargs):
    if self.version != Player.objects.get(PID=self.pk).version:
        raise Http404('Ooops!!!! Concurrency Issues, Try Again')
    super(Player, self).save(*args, **kwargs)


def savemt(self, *args, **kwargs):
    if self.version != Teams.objects.get(TeamID=self.pk).version:
        raise Http404('Ooops!!!! Concurrency Issues, Try Again')
    super(Teams, self).save(*args, **kwargs)
