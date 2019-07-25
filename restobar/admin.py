from django.contrib import admin
from .models import Team,Menu,menu_item,Reservations,Food_Type,Occasion
# Register your models here.

admin.site.register(Team)
admin.site.register(Menu)
admin.site.register(menu_item)
admin.site.register(Reservations)
admin.site.register(Food_Type)
admin.site.register(Occasion)