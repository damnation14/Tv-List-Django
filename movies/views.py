from django.shortcuts import render,redirect
import requests
import tmdbsimple as tmdb
from django.contrib.auth.models import User
from .models import tvwatched,tvwatching
#Create your views here.

tmdb.API_KEY = '7b6980485570c571af05ae41f5bb2266'


def home(request):
    if request.method=='GET' :
        tv_title = request.GET.get('keyword', False)
        if tv_title:
            search = tmdb.Search()
            response = search.tv(query=tv_title)
            tmdb_tv={'tvshows':search.results}
            return render(request, 'movies/home.html',tmdb_tv)
        else:
            return render(request, 'movies/home.html',{})

def tvdetails(request,id):
    if request.method=='GET' :
        tv = tmdb.TV(id)
        response = tv.info()
        tmdb_tv={'tvshow':tv}
        return render(request, 'movies/tvdetail.html',tmdb_tv)

def showwatched(request,id):

    if request.user.is_authenticated:
        u=User.objects.get(username=request.user.username)
        tvshows=[]
        if id!=1:
            watched=tvwatched.objects.get_or_create(
                tvid=id,
                watchers=u
            )
        show_ids=tvwatched.objects.filter(watchers=u).values_list('tvid', flat=True).order_by('id')
        for show_id in show_ids:
             t = tmdb.TV(show_id)
             t.info()
             tvshows.append(t)
        tmdb_tv={'tvshows':tvshows}
        return render(request, 'movies/watchedlist.html',tmdb_tv)

def showwatching(request,id):

    if request.user.is_authenticated:
        u=User.objects.get(username=request.user.username)
        tvshows=[]
        if id!=1:
            watched=tvwatching.objects.get_or_create(
                tvid=id,
                watchers=u
            )
        show_ids=tvwatching.objects.filter(watchers=u).values_list('tvid', flat=True).order_by('id')
        for show_id in show_ids:
             t = tmdb.TV(show_id)
             t.info()
             tvshows.append(t)
        tmdb_tv={'tvshows':tvshows}
        return render(request, 'movies/watchinglist.html',tmdb_tv)

def delshow(request,id):
    print("delete")
    u=User.objects.get(username=request.user.username)
    tvwatching.objects.filter(tvid=id).filter(watchers=u).delete()
    return redirect('tv-home')
