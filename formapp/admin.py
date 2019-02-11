from django.contrib import admin
from .models import *

class GradeModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GradeModel._meta.fields]
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = GradeModel

admin.site.register(AnswerModel)
admin.site.register(QuestionModel)
admin.site.register(StageModel)
admin.site.register(CourseModel)
admin.site.register(GradeModel, GradeModelAdmin)

# Register your models here.
