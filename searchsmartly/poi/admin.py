from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import PoI

@admin.register(PoI)
class PoIAdmin(GISModelAdmin):
    list_display = ('internal_id', 'name', 'external_id', 'category', 'avg_rating')
    search_fields = ('internal_id', 'external_id')
    list_filter = ('category',)

    def avg_rating(self, obj):
        ratings = obj.ratings
        if ratings:
            return round(sum(ratings) / len(ratings), 2)
        return 0