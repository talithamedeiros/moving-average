from django.db import models
from django.contrib.postgres.fields import JSONField

from apps.utils.models import DateModel


class Pair(DateModel):
    description = models.CharField(max_length=254, blank=True, null=True, verbose_name="Description")
    range_days = models.IntegerField(blank=True, null=True, verbose_name="Range")

    class Meta:
        verbose_name_plural = "Pair"

    def __str__(self):
        return "{}".format(self.description)


class Price(DateModel):
    pair = models.ForeignKey(Pair, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name="Pair")
    mms = models.CharField(max_length=254, blank=True, null=True, verbose_name="MMS")
    timestamp = models.CharField(max_length=254,blank=True, null=True, verbose_name="Timestamp")

    class Meta:
        verbose_name_plural = "Price"

    def __str__(self):
        return "{} - {}".format(self.pair, self.mms)
