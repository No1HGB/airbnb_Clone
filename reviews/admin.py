from operator import contains
from django.contrib import admin
from .models import Review


class WordFilter(admin.SimpleListFilter):
    title = "word"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("좋은", "좋은"),
            ("최고", "최고"),
            ("별로", "별로"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            return


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )
    list_filter = (
        WordFilter,
        "rating",
        "user__is_host",
        "room__categories",
        "room__pet_friendly",
    )
