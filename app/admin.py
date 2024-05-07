from django.contrib import admin
from .models import CarList,ShowRoomList,Review

# Register your models here.
admin.site.register([CarList,ShowRoomList,Review])