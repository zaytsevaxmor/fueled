from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()

    def __str__(self):
        return "%s" % (self.name)


class Review(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)


class Track(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User)
    restaurant = models.ForeignKey(Restaurant)