from django.db import models

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

class UserDataModel(models.Model):
    class Meta:
        db_table = 'usersdata'

    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='userid')
    name = models.CharField(max_length=30, default=None)
    last = models.CharField(max_length=30, default=None)
    age = models.PositiveSmallIntegerField(default=None)
    email = models.CharField(max_length=30, default=None)
