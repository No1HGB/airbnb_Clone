from abc import abstractclassmethod, abstractmethod
from django.db import models


class CommonModel(models.Model):

    """Common Model Def"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
