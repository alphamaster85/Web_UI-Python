from django.contrib import admin
from authapp.models import *
from .models import *

admin.site.register(UserDataModel)
admin.site.register(RoleModel)
admin.site.register(AnswerModel)
admin.site.register(QuestionModel)
admin.site.register(StageModel)
admin.site.register(CourseModel)
admin.site.register(GradeModel)

# Register your models here.
