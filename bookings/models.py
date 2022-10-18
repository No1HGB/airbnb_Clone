from random import choices
from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class Booking(CommonModel):
    class BookingKindChoices(models.TextChoices):
        ROOM = ("room", "숙소 예약")
        EXPERIENCE = ("experience", "체험 예약")

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    kind = models.CharField(
        max_length=30,
        choices=BookingKindChoices.choices,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.kind} / {self.user}"

    class Meta:
        verbose_name_plural = "예약"
