from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class Review(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    payload = models.TextField(
        default="",
        max_length=3000,
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
    )

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"

    class Meta:
        verbose_name_plural = "리뷰"
