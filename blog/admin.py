from django.contrib import admin

from  blog.models import Mytext

# Register your models here.

class MytextAdmin(admin.ModelAdmin):
    list_display = ['name','updated']

admin.site.register(Mytext,MytextAdmin)

