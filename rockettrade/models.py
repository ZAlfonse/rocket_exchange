from django.db import models


class AuctionListing(models.Model):
    # AuctionItems -- o2m auctionitem
    # Seller -- fk to auth.user
    # Buyer -- fk to auth.user
    # Open Date -- datetime
    # Closed Date -- datetime
    # Status -- fk to AuctionStatus
    pass


class AuctionStatus(models.Model):
    # name -- Completed, Open, Pending, Incomplete
    # description
    pass


class AuctionItem(models.Model):
    # item -- fk to rocketitems.item
    # quantity -- number
    # currency?
    # price
    pass
