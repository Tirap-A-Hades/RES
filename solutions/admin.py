from django.contrib import admin

from solutions.models import Solutions, Question


@admin.register(Solutions)
class SolutionAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
