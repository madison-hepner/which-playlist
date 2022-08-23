from django.db import models


class PlayListItem(models.Model):
    playlist_name = models.CharField(max_length=55)
    description = models.CharField(max_length=55)
    playlist_vibes = models.CharField(max_length=55)
    length = models.DecimalField(max_length=7, decimal_places=2, max_digits=5)
