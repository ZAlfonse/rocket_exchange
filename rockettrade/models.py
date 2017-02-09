from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser

from django.conf import settings

from rocketitems.models import Variation


class User(AbstractUser):
    steam_id = models.BigIntegerField(null=True)
    steam_persona = models.CharField(max_length=100, null=True)
    steam_profile = models.URLField(null=True)
    steam_avatar = models.URLField(null=True)
    steam_created = models.DateTimeField(blank=True, null=True)

    objects = UserManager()


class Listing(models.Model):
    OPEN = 'O'
    PENDING = 'P'
    CLOSED = 'C'
    INCOMPLETE = 'I'

    STATUS_CHOICES = (
        (OPEN, 'Open'),
        (PENDING, 'Pending'),
        (CLOSED, 'Closed'),
        (INCOMPLETE, 'Incomplete')
    )

    items = models.ManyToManyField(Variation)

    status = models.CharField(max_length=1, default=OPEN, choices=STATUS_CHOICES)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    closed = models.DateTimeField(null=True, blank=True)


class Offer(models.Model):
    listing = models.ForeignKey(Listing, related_name='offers')
    bidder = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='offers')

    items = models.ManyToManyField(Variation)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
