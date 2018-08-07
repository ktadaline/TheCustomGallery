from django.db import models

# Create your models here.
class artistProfile(models.Model):
    artist_name = models.CharField(max_length=100)
    artist_profile_pic = models.CharField(max_length=1000)
    artist_genres = models.CharField(max_length=500)
    artist_description = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
        return self.artist_name

class artistPortfolio(models.Model):
    artist = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    art_title = models.CharFirld(max_length=250)
    art_image = models.CharField(max_length=1000)

    def __str__(self):
        return self.art_title + '-' + self.art_image