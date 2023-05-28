from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField

class Videos(models.Model):
    video = EmbedVideoField()  # same like models.URLField()

class Video_2(models.Model):
    video_2 = EmbedVideoField()