

from django.contrib import admin
from .models import Profile
# to display in admin panel
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'hackerrank_id', 'streak', 'name']

admin.site.register(Profile, ProfileAdmin)

