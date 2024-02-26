

from django.contrib import admin
from .models import Profile
# to display in admin panel
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'hackerrank_id', 'c1progress','c2progress', 'name','imguploadlimit','image']

admin.site.register(Profile, ProfileAdmin)

