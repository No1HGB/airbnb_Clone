from tabnanny import verbose
from django.db import models
from common.models import CommonModel


class ChattingRoom(CommonModel):
    name = models.CharField(
        max_length=15,
        default="이름없는 채팅방",
    )
    user = models.ManyToManyField(
        "users.User",
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "채팅방"


class Message(CommonModel):
    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return "DM"

    class Meta:
        verbose_name_plural = "DM"
