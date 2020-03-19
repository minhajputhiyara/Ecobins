from django.contrib import admin
from .models import GarbageCategory,Garbage


#this is to customize garbage admin model display
class GarbageAdmin(admin.ModelAdmin):

    list_display = ['__str__', 'slug',]

    class Meta:
        model=Garbage


admin.site.register(Garbage,GarbageAdmin)
admin.site.register(GarbageCategory)