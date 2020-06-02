from django.shortcuts import get_object_or_404, redirect, render
from .models import Teams, Player, Series, Match
from django.http import Http404
from .forms import TeamForm, PlayerForm, SeriesForm, MatchForm


# Create your views here.
def index(request):
    context = {'all_teams': Teams.objects.all()}
    return render(request, 'teams/index.html', context)


def details(request, teamID):
    try:
        team: object = Teams.objects.get(pk=teamID)
    except Teams.DoesNotExist:
        raise Http404("Team is not registered")
    return render(request, 'teams/details.html', {'team': team})


def players(request, teamID):
    try:
        pl: object = Player.objects.filter(TeamID_id=teamID)
    except Player.DoesNotExist:
        raise Http404("No Registered Players in the Team")
    return render(request, 'teams/retplayers.html', {'pl': pl})


def home(request):
    return render(request, 'teams/home.html', {})


def TeamCreate(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, 'teams/teams_create.html', context)


def series_index(request):
    context = {'all_series': Series.objects.all()}
    return render(request, 'teams/series_index.html', context)


def series_details(request, seriesID):
    try:
        ser: object = Series.objects.get(pk=seriesID)
    except Series.DoesNotExist:
        raise Http404("Series is not registered")
    return render(request, 'teams/series_details.html', {'ser': ser})


def matches(request, seriesID):
    try:
        ml: object = Match.objects.filter(SeriesID_id=seriesID)
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
        form.save()
        form = SeriesForm()
    context = {
        'form': form
    }
    return render(request, 'teams/series_create.html', context)


def seriesdelete(request, seriesID):
    try:
        t: object = Series.objects.filter(SeriesID=seriesID)
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
        form.save()
        form = MatchForm()
    context = {
        'form': form
    }
    return render(request, 'teams/series_create.html', context)


def matchdelete(request, matchID):
    try:
        t: object = Match.objects.filter(MatchID=matchID)
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
        form.save()
        form = TeamForm()
    context = {
        'form': form
    }
    return render(request, 'teams/teams_create.html', context)


def teamdelete(request, teamID):
    try:
        t: object = Teams.objects.filter(TeamID=teamID)
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
        form.save()
        form = TeamForm()
    context = {
        'form': form
    }
    return render(request, 'teams/teams_create.html', context)


def playerdelete(request, pid):
    try:
        t: object = Player.objects.filter(PID=pid)
    except Player.DoesNotExist:
        raise Http404("Please Select a valid player to remove")
    deleted = t.delete()
    if deleted:
        return render(request, 'series1/match_confirm_delete.html', )
    else:
        raise Http404(" Sorry, we could not delete the given team")
