from django.contrib import admin

# Register your models here.
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Videos,Video_2

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Videos, MyModelAdmin)


