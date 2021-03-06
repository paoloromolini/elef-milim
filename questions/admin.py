from django.contrib import admin
from .models import Lesson, Question

class QuestionInline(admin.TabularInline):
    model = Question

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline, ]


admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question)