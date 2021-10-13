from django.db import models

from model_utils.models import SoftDeletableModel


class DateModel(SoftDeletableModel):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True