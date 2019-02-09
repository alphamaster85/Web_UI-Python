from django.db import models
from django.conf import settings

class GradeModel(models.Model):
    class Meta:
        db_table = 'grade'

    name = models.CharField(max_length=20, default=None)

class CourseModel(models.Model):
    class Meta:
        db_table = 'course'

    name = models.CharField(max_length=20, default=None)

class StageModel(models.Model):
    class Meta:
        db_table = 'stage'

    department = models.CharField(max_length=20, default=None)
    name = models.CharField(max_length=50, default=None)

class QuestionModel(models.Model):
    class Meta:
        db_table = 'question'

    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    stage = models.ForeignKey(StageModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default=None)
    tooltip = models.TextField(max_length=350, null=True, default=None)

class AnswerModel(models.Model):
    class Meta:
        db_table = 'answer'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    question = models.ForeignKey(QuestionModel, on_delete=models.DO_NOTHING)
    like = models.NullBooleanField(default=None, null=True)
    grade = models.ForeignKey(GradeModel, on_delete=models.DO_NOTHING, default=None, null=True)
    date = models.DateTimeField(default=None, null=True)

class CommentExpModel(models.Model):
    class Meta:
        db_table = 'comment'

    expert = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    answer = models.ForeignKey(AnswerModel, on_delete=models.CASCADE)
    grade = models.ForeignKey(GradeModel, on_delete=models.DO_NOTHING, default=None)
    title = models.CharField(max_length=250, default=None)
    date = models.DateTimeField()
