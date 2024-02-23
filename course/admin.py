from django.contrib import admin
from .models import Answers

# Register your models here.
class AnswersAdmin(admin.ModelAdmin):
    list_display = ['topic','que1','que2','prgrscontribution']

admin.site.register(Answers, AnswersAdmin)
