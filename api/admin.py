from django.contrib import admin
from api.models import Restaurant, Review, Track

class RestaurantAdmin(admin.ModelAdmin):
    pass
admin.site.register(Restaurant, RestaurantAdmin)

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, ReviewAdmin)

class TrackAdmin(admin.ModelAdmin):
    pass
admin.site.register(Track, TrackAdmin)
