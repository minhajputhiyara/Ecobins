from django.contrib import admin

# Register your models here.
from .models import Complain,Notification


admin.site.register(Complain)
admin.site.register(Notification)