from django.db import models
from django.contrib.auth.models import User

from rocketitems.models import Item


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
	
    item = models.ManyToManyField(Item, through='ListItem')
    seller = models.ForeignKey(User)
    
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    closed = models.DateTimeField()
    
    def value(self):
        self.item.quanity * self.item.price

    def __str__(self):
    	return '%s\'s offer of %i %s for %s' % self.seller.username, self.item.quantity, self.item.name, self.value


class ListItem(models.Model):
    item = models.ForeignKey(Item)
    auction = models.ForeignKey(AuctionListing)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9, decimal_places=4)
