from django.db import models


class Rarity(models.Model):
    name = models.CharField(max_length=20, unique=True)
    rank = models.IntegerField(default=-1)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rarity = models.ForeignKey(Rarity)
    category = models.ForeignKey(Category)
    # image = models.ImageField()
    pc_only = models.BooleanField(default=False)
    xbox_only = models.BooleanField(default=False)
    psn_only = models.BooleanField(default=False)

    def platform_restrictions(self):
        restrictions = []

        if self.pc_only:
            restrictions.append('pc_only')
        if self.xbox_only:
            restrictions.append('xbox_only')
        if self.psn_only:
            restrictions.append('psn_only')

        return restrictions

    def __str__(self):
        return self.name
