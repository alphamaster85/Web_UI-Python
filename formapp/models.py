from django.db import models
import datetime

class RoleModel(models.Model):
    class Meta:
        db_table = 'roles'

    role = models.CharField(max_length=30, default=None)

class UserDataModel(models.Model):
    class Meta:
        db_table = 'usersdata'

    name = models.CharField(max_length=30, default=None)
    last = models.CharField(max_length=30, default=None)
    age = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=30, default=None)
    date = models.DateTimeField('date')

class UserModel(models.Model):
    class Meta:
        db_table = 'users'

    login = models.CharField(max_length=30, default=None)
    password = models.CharField(max_length=30, default=None)
    user = models.OneToOneField(UserDataModel, on_delete = models.CASCADE, related_name='userid')
    role = models.ForeignKey(RoleModel, on_delete = models.DO_NOTHING)

class GradesModel(models.Model):
    class Meta:
        db_table = 'grades'

    grade = models.CharField(max_length=20, default=None)

class CourseModel(models.Model):
    class Meta:
        db_table = 'courses'

    course = models.CharField(max_length=20, default=None)

class StageModel(models.Model):
    class Meta:
        db_table = 'stages'

    part = models.CharField(max_length=20, default=None)
    stage = models.CharField(max_length=50, default=None)

class QuestionModel(models.Model):
    class Meta:
        db_table = 'questions'

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE)
    qestion = models.CharField(max_length=50, default=None)

class AnswerModel(models.Model):
    class Meta:
        db_table = 'answers'

    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(QuestionModel, on_delete=models.DO_NOTHING)
    like = models.NullBooleanField(default=None)
    grade = models.ForeignKey(GradesModel, on_delete=models.DO_NOTHING, default=None)
    date = models.DateTimeField()

class CommentExpModel(models.Model):
    class Meta:
        db_table = 'comments'

    #user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    expert = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(AnswerModel, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradesModel, on_delete=models.DO_NOTHING, default=None)
    comment = models.CharField(max_length=250, default=None)
    date = models.DateTimeField()
