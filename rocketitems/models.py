from django.db import models


class Quality(models.Model):
    name = models.CharField(max_length=20, unique=True)
    sort = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Pack(models.Model):
    name = models.CharField(max_length=20, unique=True)
    release_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    CERTIFIED = 'C'
    PAINTED = 'P'
    TYPE_CHOICES = (
        (CERTIFIED, 'Certified'),
        (PAINTED, 'Painted')
    )
    name = models.CharField(max_length=50)
    type = models.CharField(choices=TYPE_CHOICES, max_length=1)
    description = models.CharField(default="An item modifier", max_length=50)

    class Meta:
        unique_together = ('name', 'type',)

    def __str__(self):
        return self.get_type_display() + ' - ' + self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    quality = models.ForeignKey(Quality)
    type = models.ForeignKey(Type)
    pack = models.ForeignKey(Pack)
    # image = models.ImageField()
    pc_only = models.BooleanField(default=False)
    xbox_only = models.BooleanField(default=False)
    psn_only = models.BooleanField(default=False)

    @property
    def image_url(self):
        return 'http://lorempixel.com/100/100/abstract/{}/'.format(self.name)

    class Meta:
        unique_together = ('name', 'type',)

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
        return str(self.type) + ' - ' + self.name


class Variation(models.Model):
    item = models.ForeignKey(Item, related_name='variations')

    def __str__(self):
        return ', '.join([attr.attribute.name for attr in self.attributes.all()]) + ' ' + self.item.name


class VariationAttribute(models.Model):
    variation = models.ForeignKey(Variation, related_name='attributes')
    attribute = models.ForeignKey(Attribute)

    class Meta:
        unique_together = ('variation', 'attribute',)
