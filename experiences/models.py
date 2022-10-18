from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class Experience(CommonModel):
    """Experience Model Def"""

    name = models.CharField(
        max_length=30,
    )
    country = models.CharField(
        max_length=50,
        default="대한민국",
    )
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    host = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    description = models.TextField()
    price = models.PositiveIntegerField()
    address = models.CharField(
        max_length=150,
    )
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField(
        "experiences.Perk",
    )
    categories = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "활동"


class Perk(CommonModel):
    """What is included on an Experience"""

    name = models.CharField(
        max_length=30,
    )
    details = models.CharField(
        max_length=250,
        blank=True,
        default="",
    )
    explanation = models.TextField(
        blank=True,
        default="",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "체험"
