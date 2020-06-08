from django.shortcuts import get_object_or_404, redirect, render
from .models import Teams, Player, Series, Match
from django.http import Http404,HttpResponsePermanentRedirect
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
    return HttpResponsePermanentRedirect(reverse('Player-Update', args=(pk1)))
    return HttpResponsePermanentRedirect(reverse('PLayer-Delete', args=(pk1)))

def search(request):
    if request.method == 'POST':
        form = searchform(request.POST)
        if form.is_valid():
            searchvalue = form.cleaned_data['searchvalue']
            type1 = form.cleaned_data['type1']



            context = {
                't': Teams.objects.all().filter(TeamName__contains=searchvalue),
                'p': Player.objects.all().filter(PName__contains=searchvalue),
                's': Series.objects.all().filter(SeriesName__contains=searchvalue),



            }
            if int(type1) == 1:
                return render(request,'teams/search_result_1.html',context)
            elif int(type1) == 2:
                return render(request, 'teams/search_result_2.html', context)
            elif int(type1) == 3:
                return render(request, 'teams/search_result_3.html', context)
            else:
                return render(request, 'teams/search_result_4.html', context)
    else:
        form = searchform()
    return render(request, 'teams/form.html', {'form': form})


def searchresult(request, searchvalue, type1):
    context = {
        't': Teams.objects.all().filter(TeamName__icontains=searchvalue),
        'p': Player.objects.all().filter(PName__icontains=searchvalue),
        's': Series.objects.all().filter(SeriesName__icontains=searchvalue),
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
            return redirect('/teams/series/')
    else:
        form = matchform()
    context = {'form': form, }
    return render(request, 'teams/form.html', context)






def TeamUpdate(request, pk1):
    team = get_object_or_404(Teams, pk=pk1)
    if request.method == 'POST':
        form = teamsform(request.POST or None)
        if form.is_valid():
            team.TeamName = form.cleaned_data['TeamName']
            team.save()
       # return redirect('/teams/')
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
        #return reverse('/teams/')

    else:
        form = playerform()
    context = {'form': form, }
    return render(request, 'teams/form.html', context)


def PlayerUpdate1(request, pid):
    player = get_object_or_404(Player, pk=pid)
    if request.method == 'POST':
        form = playerform(request.POST or None)

        if form.is_valid():
            player.PName = form.cleaned_data['PName']
            player.PAge = form.cleaned_data['PAge']
            player.PType = form.cleaned_data['PType']
            player.Team = form.cleaned_data['Team']
            player.save()
        #return redirect('/teams/')
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
    d = False
    if request.method == 'POST':
        form= match_result_form(request.POST)


        if form.is_valid():
           for f in tm:
               if f.TeamName == form.cleaned_data['TeamName']:
                    d=True

           if d == True:
                m.WinningTeam = form.cleaned_data['TeamName']
                a = Teams.objects.get(TeamName__exact= m.WinningTeam)
                a. Points = a.Points +3
                a.save()
                m.save()
    else:
        if(m.WinningTeam == 'NoTeam'):
            form = match_result_form()

        else:
            return Http404('Team Result Already Decided')
    context ={
        'form' : form
    }
    return render(request, 'teams/form.html',context)





