from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    class CategoryKindChoices(models.TextChoices):
        ROOM = ("room", "숙소")
        EXPERIENCE = ("experience", "체험")

    name = models.CharField(max_length=30)
    kind = models.CharField(
        max_length=10,
        choices=CategoryKindChoices.choices,
    )

    class Meta:
        verbose_name_plural = "분류"

    def __str__(self) -> str:
        return f"{self.kind.title()}: {self.name}"
