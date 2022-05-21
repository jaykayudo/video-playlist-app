from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Playlist,Moviename
from django.views.generic.edit import UpdateView

def index(request):
    playlist = Playlist.objects.all()
    template = loader.get_template('video/index.html')
    playlists = {'playlist':playlist}
    
    return render(request,'video/index.html',{'playlist':playlist})
def details(request,play_id):
    play = get_object_or_404(Playlist,main_character = play_id)
    return render(request,'video/details.html',{'play':play})
def favorite(request,play_id):
    play = get_object_or_404(Playlist,main_character = play_id)
    vid = request.POST['video']
    vido = Moviename.objects.get(movie = vid)
    vido.is_favorite = True
    vido.save()
    return render(request,'video/details.html',{'play':play})
def video_list(request):
    vid = Moviename.objects.all()
    return render(request,'video/videoslist.html',{'vid':vid})
def form(request):
    return render(request,'video/playlistform.html',{'none':'none'})
def addform(request):
    vid = Playlist()
    vid.main_character = request.POST['actor']
    vid.genre = request.POST['genre']
    vid.logo = request.POST['logo']
    vid.save()
    return redirect('/video/')
class PlaylistUpdate(UpdateView):
    model = Playlist()
    fields = ['main_character','genre','logo']


