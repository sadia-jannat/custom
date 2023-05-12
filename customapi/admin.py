from django.contrib import admin

# Register your models here.
from customapi.models import CustomUser
admin.site.register(CustomUser)
