from django.contrib import admin

# Register your models here.
from . models import Transcactions
from . models import profile

admin.site.register(Transcactions)
admin.site.register(profile)