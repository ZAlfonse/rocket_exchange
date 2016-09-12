from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from django.conf import settings

from rocketitems.models import Item


class User(AbstractUser):
    steam_id = models.BigIntegerField(null=True)
    steam_persona = models.CharField(max_length=100, null=True)
    steam_username = models.CharField(max_length=50, null=True)

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

    status = models.CharField(max_length=1, default=OPEN, choices=STATUS_CHOICES)

    item = models.ForeignKey(Item)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=9, decimal_places=4)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases', null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    closed = models.DateTimeField(null=True, blank=True)

    @property
    def value(self):
        return self.quantity * self.price

    def __str__(self):
        return '{}\'s listing of {} {} @ {} for {}'.format(self.seller.username, self.quantity, self.item.name, self.price, self.value)
