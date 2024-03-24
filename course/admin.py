from django.contrib import admin
from .models import Answers,userprogress

# Register your models here.
class AnswersAdmin(admin.ModelAdmin):
    list_display = ['topic','que1','que2']

class UserprogressAdmin(admin.ModelAdmin):
    list_display = ['user', 'completed_topics']

    def completed_topics(self, obj):
        completed_topics = obj.completed_topic.all()
        return ", ".join([answer.topic for answer in completed_topics])

admin.site.register(userprogress, UserprogressAdmin)
admin.site.register(Answers, AnswersAdmin)
