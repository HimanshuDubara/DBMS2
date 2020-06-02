from django.conf.urls import url

from .import views

app_name = "teams"


urlpatterns = (
                  # /teams/
                  url(r'^$', views.index, name='index'),

                  # /teams/teamID
                  url(r'^(?P<teamID>[0-9]+)/$', views.details, name='details'),

                  # /teams/TeamID/players
                  url(r'^(?P<teamID>[0-9]+)/players$', views.players, name='players'),
                  # /teams/add/
                  url(r'^add/$', views.TeamCreate, name='Team-Add'),

                  # /teams/teamID/update/
                  url(r'^(?P<pk1>[0-9]+)/update/$', views.TeamUpdate, name='Team-Update'),

                  # /teams/teamID/delete/
                  url(r'^(?P<teamID>[0-9]+)/delete/$', views.teamdelete, name='Team-Delete'),

                  # /teams/add_player/
                  url(r'^add_player/$', views.PlayerCreate, name='Player-Add'),

                  #/teams/players/pid/update/
                  url(r'^players/(?P<pk1>[0-9]+)/update/$', views.PlayerUpdate, name='Player-Update'),

                  #/teams/players/pid/delete/
                  url(r'^players/(?P<pid>[0-9]+)/delete/$', views.playerdelete, name='Player-Delete'),

                  # teams/series/
                  url(r'^series/$', views.series_index, name='index'),

                  # teams/series/seriesID/
                  url(r'^series/(?P<seriesID>[0-9]+)/$', views.series_details, name='details'),

                  # teams/series/seriesID/matches/
                  url(r'^series/(?P<seriesID>[0-9]+)/matches/$', views.matches, name='matches'),
                  # series/series/add/
                  url(r'series/add/$', views.SeriesCreate, name='Series-Add'),

                  # teams/series/seriesID/update/
                  url(r'series/(?P<pk1>[0-9]+)/update/$', views.SeriesUpdate, name='Series-Update'),

                  # teams/series/seriesID/delete/
                  url(r'^series/(?P<seriesID>[0-9]+)/delete/$', views.seriesdelete, name='Series-Delete'),

                  # teams/series/add_match/
                  url(r'^series/add_match/$', views.MatchCreate, name='MatchCreate'),

                  #teams/series/matches/matchID/update/
                  url(r'^series/(?P<pk1>[0-9]+)/update/$', views.MatchUpdate, name='Match-Update'),

                  #teams/series/matches/matchID/delete/
                  url(r'^series/matches/(?P<matchID>[0-9]+)/delete/$', views.matchdelete, name='Match-Delete'),

)

