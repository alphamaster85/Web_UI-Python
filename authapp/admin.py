from django.contrib import admin
from .models import *

class UserDataModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserDataModel._meta.fields]
    list_filter = ['name']
    search_fields = ['login', 'name', 'last']

    class Meta:
        model = UserDataModel

class RoleModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RoleModel._meta.fields]
    list_filter = ['name']
    search_fields = ['name']

    class Meta:
        model = RoleModel

admin.site.register(UserDataModel, UserDataModelAdmin)
admin.site.register(RoleModel, RoleModelAdmin)

# Register your models here.
