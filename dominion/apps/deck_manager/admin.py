from django.contrib import admin
from .models import User as U, Kingdom, Kingdoms_Cards, Card, Game, Rating

# Register your models here.
class KingdomAdmin(admin.ModelAdmin):
	pass
admin.site.register(Kingdom, KingdomAdmin)

class CardAdmin(admin.ModelAdmin):
	pass
admin.site.register(Card, CardAdmin)

class UGameAdmin(admin.ModelAdmin):
	pass
admin.site.register(Game, UGameAdmin)

class RatingAdmin(admin.ModelAdmin):
	pass
admin.site.register(Rating, RatingAdmin)

class Kingdoms_CardsAdmin(admin.ModelAdmin):
	pass
admin.site.register(Kingdoms_Cards, Kingdoms_CardsAdmin)