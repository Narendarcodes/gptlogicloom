

from django.contrib import admin
from .models import Profile,Badge
# to display in admin panel
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'nickname', 'hackerrank_id', 'c1progress','c2progress', 'name','imguploadlimit','image']

admin.site.register(Profile, ProfileAdmin)


class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'display_image')  # Add other fields as needed
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return obj.image.url if obj.image else None

admin.site.register(Badge, BadgeAdmin)