from django.contrib import admin
from .models import Badge

class BadgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image_preview')  
    readonly_fields = ('image_preview',)  

    def image_preview(self, obj):
        return obj.image.url if obj.image else None 

    image_preview.short_description = 'Image'  

admin.site.register(Badge, BadgeAdmin)
