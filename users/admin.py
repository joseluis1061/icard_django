from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import User

# from django.contrib.auth.admin import UserAdmin
# admin.site.register(User, UserAdmin)

@admin.register(User)
class UserAdmin(BaseAdmin):
  pass