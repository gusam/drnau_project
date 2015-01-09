from django.contrib import admin

from .models import Project,ShowTv,Schedule,Prototype

# Register your models here.
admin.site.register(Project)
admin.site.register(ShowTv)
admin.site.register(Schedule)
admin.site.register(Prototype)