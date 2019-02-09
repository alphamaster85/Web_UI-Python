from django.db import models
from django.conf import settings

class RoleModel(models.Model):
    class Meta:
        db_table = 'roles'

    name = models.CharField(max_length=30, default=None)

class UserModel(models.Model):
    class Meta:
        db_table = 'users'

    login = models.CharField(max_length=30, default=None)
    password = models.CharField(max_length=30, default=None)
    role = models.ForeignKey(RoleModel, on_delete = models.DO_NOTHING)
    date = models.DateField(default=None)
    auth_django = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)

class UserDataModel(models.Model):
    class Meta:
        db_table = 'usersdata'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='userid')
    name = models.CharField(max_length=30, default=None, null=True)
    last = models.CharField(max_length=30, default=None, null=True)
    age = models.PositiveSmallIntegerField(default=None, null=True)
    email = models.CharField(max_length=30, default=None, null=True)
