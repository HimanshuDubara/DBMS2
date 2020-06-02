from django.contrib import admin
from .models import Teams,Player,Series,Match
# Register your models here.
admin.site.register(Teams)
admin.site.register(Player)
admin.site.register(Series)
admin.site.register(Match)