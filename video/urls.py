from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'video'

urlpatterns = [
    url('^$', views.index,name = 'index'),
    url('^video list/$',views.video_list,name='videolist'),
    url('^add/$',views.form,name='add'),
    url('^(?P<play_id>.+)/$',views.details,name='details'),
    url('^(?P<play_id>.+)/favorite$',views.favorite,name='favor'),
    url('^add/save$',views.addform,name='form'),
    url('^playlist/update$',views.PlaylistUpdate.as_view(),name='update'),
    
    
]
