from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

from tournament import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players/$', views.PlayerList.as_view()),
    url(r'^players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view()),
    url(r'^tournaments/$', views.TournamentList.as_view()),
    url(r'^tournaments/(?P<pk>[0-9]+)/$', views.TournamentDetail.as_view()),
    url(r'^matches/$', views.MatchList.as_view()),
    url(r'^matches/(?P<pk>[0-9]+)/$', views.MatchDetail.as_view()),
    url(r'^entries/$', views.EntryList.as_view()),
    url(r'^entries/(?P<pk>[0-9]+)/$', views.EntryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
