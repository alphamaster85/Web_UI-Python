from django.contrib import admin
from .models import UserModel, AnswerModel

admin.site.register(UserModel)
# admin.site.register(UserDataModel)
admin.site.register(AnswerModel)

# Register your models here.
