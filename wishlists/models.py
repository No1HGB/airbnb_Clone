from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):

    name = models.CharField(max_length=50)
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "위시리스트"

    def __str__(self) -> str:
        return self.name
