from django.db import models


# Create your models here.
class Place(models.Model):
    names = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    description = models.TextField()

    def __str__(self):
        return self.names


class Team(models.Model):
    member_name = models.CharField(max_length=250)
    member_img = models.ImageField(upload_to='team_pics')
    member_details = models.TextField()

    def __str__(self):
        return self.member_name
