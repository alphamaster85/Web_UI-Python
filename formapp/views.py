from django.http import HttpResponse
from django.shortcuts import render
from .models import StageModel, QuestionModel, AnswerModel, GradeModel
# from authapp.models import UserModel
from bulk_update.helper import bulk_update
import datetime
USER_ID = 1

def formapp(request):

    stages = StageModel.objects.all()
    questions = QuestionModel.objects.all()
    departments = ['Activities', 'Skills']  # list(set(StageModel.objects.all()))
    answers = AnswerModel.objects.filter(user_id=USER_ID)
    grades = GradeModel.objects.all()

    i = 1; j = 1; skills_first = None
    stage_indexes = {}
    for stage in stages:
        if stage.department == departments[0]:
            stage_indexes[stage.id] = i
            i += 1
        if stage.department == departments[1]:
            stage_indexes[stage.id] = j
            if j == 1:
                skills_first = stage.id
                print(skills_first)
            j += 1

    if request.method == "POST":

        all_answers = []
        for answer in answers:

            if request.POST.get('set_like_' + str(answer.question_id)):
                answer.like = request.POST.get('set_like_' + str(answer.question_id))
            if request.POST.get('set_grade_' + str(answer.question_id)):
                answer.grade_id = int(request.POST.get('set_grade_' + str(answer.question_id)))
            answer.date = datetime.date.today()
            all_answers.append(answer)

        bulk_update(answers)
        answers = AnswerModel.objects.filter(user=USER_ID)

    return render(request, "index.html", context={'questions':questions, 'stages':stages, 'departments':departments, 'answers':answers, 'grades':grades, 'stage_indexes':stage_indexes, 'skills_first':skills_first})



