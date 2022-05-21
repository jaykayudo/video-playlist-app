from django.db import models
from django.urls import reverse

class Playlist(models.Model):
    main_character = models.CharField(max_length=250)
    genre = models.CharField(max_length=250)
    logo = models.FileField()

    def get_absolute_url(self):
        return reverse('video:index')

    def __str__(self):
        return self.main_character + ' - ' + self.genre
    


class Moviename(models.Model):
    playlist = models.ForeignKey(Playlist,on_delete=models.CASCADE)
    movie = models.CharField(max_length=1000)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.movie
