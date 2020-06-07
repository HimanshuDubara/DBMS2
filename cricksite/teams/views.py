from django.shortcuts import get_object_or_404, redirect, render
from .models import Teams, Player, Series, Match
from django.http import Http404,HttpResponseRedirect
from .forms import teamsform, playerform, seriesform, matchform, searchform,match_result_form
from datetime import date
from django.urls import reverse


# Create your views here.
def index(request):
    context = {'all_teams': Teams.objects.all().order_by('-Points')}
    return render(request, 'teams/index.html', context)


def details(request, teamID):
    try:
        team: object = Teams.objects.get(pk=teamID)
    except Teams.DoesNotExist:
        raise Http404("Team is not registered")
    return render(request, 'teams/details.html', {'team': team})


def players(request, teamID):
    try:
        pl: object = Player.objects.filter(Team=teamID).order_by('pk')
    except Player.DoesNotExist:
        raise Http404("No Registered Players in the Team")
    return render(request, 'teams/retplayers.html', {'pl': pl})


def search(request):
    if request.method == 'POST':
        form = searchform(request.POST)
        if form.is_valid():
            searchvalue = form.cleaned_data['searchvalue']
            type1 = form.cleaned_data['type1']

            return redirect('/teams/search_result/'+ str(searchvalue)+'/'+str(type1)+'/')
    else:
        print('Hello')
        form = searchform()
        print(form)
    return render(request, 'teams/form.html', {'form': form})


def searchresult(request, searchvalue, type1):
    context = {
        't': Teams.objects.all().filter(TeamName__contains=searchvalue),
        'p': Player.objects.all().filter(PName__contains=searchvalue),
        's': Series.objects.all().filter(SeriesName__contains=searchvalue),
        'type1': type1
    }
    return render(request, 'teams/search_result.html', context)


def TeamCreate(request):
    if request.method == 'POST':
        form = teamsform(request.POST)
        print(form)
        team = Teams()
        if form.is_valid():
            print(form.cleaned_data)
            team.TeamName = form.cleaned_data['TeamName']

            team.save()
            return redirect('/teams/')
    else:
        form = teamsform()
    context = {'form': form}

    return render(request, 'teams/form.html', context)


def series_index(request):
    context = {'all_series': Series.objects.all().order_by('pk')}
    return render(request, 'teams/series_index.html', context)


def series_details(request, seriesID):
    try:
        ser = Series.objects.get(pk=seriesID)
    except Series.DoesNotExist:
        raise Http404("Series is not registered")
    return render(request, 'teams/series_details.html', {'ser': ser, 'ts': ser.Teams.all()})


def matches(request, seriesID):
    try:
        pendingmatches  = Match.objects.filter(Series=seriesID,MatchDate__gt=date.today())
        donematches = Match.objects.filter(Series=seriesID,MatchDate__lte=date.today())
    except Series.DoesNotExist:
        raise Http404("No Registered Matches in the Series")
    return render(request, 'teams/retmatches.html', {'pendingmatches' : pendingmatches,'donematches': donematches})


def SeriesCreate(request):
    if request.method == 'POST':
        form = seriesform(request.POST)
        series = Series()
        if form.is_valid():
            print(form.cleaned_data['Teams'])
            series.SeriesName = form.cleaned_data['SeriesName']
            series.StartDate = form.cleaned_data['StartDate']
            series.EndDate = form.clean_EndDate()
            series.save()
            for f in form.cleaned_data['Teams']:
                series.Teams.add(f)
            return redirect('/teams/series/')
    else:
        form = seriesform()
    context = {'form': form}

    return render(request, 'teams/form.html', context)


def SeriesUpdate(request, pk1):
    series = get_object_or_404(Series, pk=pk1)
    if request.method == 'POST':
        form = seriesform(request.POST)
        if form.is_valid():
            series.SeriesName = form.cleaned_data['SeriesName']
            series.StartDate = form.cleaned_data['StartDate']
            series.EndDate = form.clean_EndDate()

            series.save()
            for f in form.cleaned_data['Teams']:
                series.Teams.add(f)
            return redirect('/teams/series/')
    else:
        forms = seriesform()
    context = {
        'form': form,
        'series': series
    }
    return render(request, 'teams/form.html', context)


def seriesdelete(request, seriesID):
    try:
        t: object = Series.objects.get(pk=seriesID)
    except Series.DoesNotExist:
        raise Http404("Please Select a valid Series to remove")
    deleted = t.delete()
    if deleted:
        return redirect('/teams/series/')
    else:
        raise Http404(" Sorry, we could not delete the given Series")


def MatchCreate(request):
    if request.method == 'POST':
        form = matchform(request.POST)
        match = Match()
        if form.is_valid():
            match.Series = form.cleaned_data['Series']
            match.MatchDate = form.cleaned_data['MatchDate']
            match.save()
            for f in form.cleaned_data['Teams']:
                match.Teams.add(f)
            return reverse('/teams/series/')
    else:
        form = matchform()
    context = {'form': form, }
    return render(request, 'teams/form.html', context)


def MatchUpdate(request, pk1):
    match = get_object_or_404(Match, pk=pk1)
    if request.method == 'POST':
        form = matchform(request.POST or None)
        match = Match()
        if form.is_valid():
            match.Series = form.cleaned_data['Series']
            match.MatchDate = form.cleaned_data['MatchDate']
            match.save()
            for f in form.cleaned_data['Teams']:
                match.Teams.add(f)
    else:
        form = matchform()
    context = {
        'form': form,
        'match': match,
    }
    return render(request, 'teams/form.html', context)


def matchdelete(request, matchID):
    try:
        t: object = Match.objects.get(pk=matchID)
    except Match.DoesNotExist:
        raise Http404("Please Select a valid match to remove")
    deleted = t.delete()
    if deleted:
        return redirect('teams/series/')
    else:
        raise Http404(" Sorry, we could not delete the given match")


def TeamUpdate(request, pk1):
    team = get_object_or_404(Teams, pk=pk1)
    if request.method == 'POST':
        form = teamsform(request.POST or None)
        if form.is_valid():
            team.TeamName = form.cleaned_data['TeamName']
            team.save()
        return reverse('/teams/')
    else:
        form = teamsform()
    context = {'form': form,
               'team': team,
               }
    return render(request, 'teams/form.html', context)


def teamdelete(request, teamID):
    try:
        t: object = Teams.objects.get(pk=teamID)
    except Player.DoesNotExist:
        raise Http404("Please Select a valid team to remove")
    deleted = t.delete()
    if deleted:
        return redirect('/teams/')
    else:
        raise Http404(" Sorry, we could not delete the given team")


def PlayerCreate(request):
    if request.method == 'POST':
        form = playerform(request.POST)
        player = Player()
        if form.is_valid():
            player.PName = form.cleaned_data['PName']
            player.PAge = form.cleaned_data['PAge']
            player.PType = form.cleaned_data['PType']
            player.Team = form.cleaned_data['Team']
            player.save()
        return reverse('/teams/')

    else:
        form = playerform()
    context = {'form': form, }
    return render(request, 'teams/form.html', context)


def PlayerUpdate(request, pk1):
    player = get_object_or_404(Player, pk=pk1)
    if request.method == 'POST':
        form = playerform(request.POST or None)

        if form.is_valid():
            player.PName = form.cleaned_data['PName']
            player.PAge = form.cleaned_data['PAge']
            player.PType = form.cleaned_data['PType']
            player.Team = form.cleaned_data['Team']
            player.save()
        return reverse('/teams/')
    else:
        form = playerform()
    context = {'form': form,
               'player': player,
               }
    return render(request, 'teams/form.html', context)


def playerdelete(request, pid):
    try:
        t: object = Player.objects.get(pk=pid)
    except Player.DoesNotExist:
        raise Http404("Please Select a valid player to remove")
    deleted = t.delete()
    if deleted:
        return redirect('teams/')
    else:
        raise Http404(" Sorry, we could not delete the given team")

def matchteams(request, matchID):
    t = Match.objects.get(pk=matchID).Teams.all()

    return render(request,'teams/match_teams.html',{'t':t,'matchID':matchID})

def matchdecide(request,matchID):
    m = Match.objects.get(pk = matchID)
    tm = m.Teams.all()

    if request.method == 'POST':
        form = match_result_form(request.POST)
        if form.is_valid():
            m.WinningTeam = form.cleaned_data['Team_Name']
            a = Teams.objects.get(TeamName__exact= m.WinningTeam)
            a. Points = a.Points +3
            a.save()
            m.save()
    else:
        if(m.WinningTeam == 'NoTeam'):
            form = match_result_form(tm)
        else:
            return Http404('Team Result Already Decided')
    context ={
        'form' : form
    }
    return render(request, 'teams/form.html',context)





