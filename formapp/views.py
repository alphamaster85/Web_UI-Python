from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import StageModel, QuestionModel, AnswerModel, GradeModel
from authapp.models import UserDataModel
from bulk_update.helper import bulk_update
import datetime
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# main function of this view
@login_required(login_url='home')
def formapp(request, user_id):

    stages = StageModel.objects.all()
    questions = QuestionModel.objects.all()
    departments = (StageModel.objects.all())
    answers = AnswerModel.objects.filter(user_id=user_id)
    grades = GradeModel.objects.all()
    user = UserDataModel.objects.get(user=user_id)
    user_name = '{} {}'.format(user.name, user.last)

    #take losf of departmets: Activities & Skills
    parts = []
    for department in departments:
        parts.append(department.department)
    departments = sorted(list(set(parts)))

    #take dict with numbers of stages in departmets Activities or Skills
    i = 1; j = 1; skills_first = None
    for stage in stages:
        if stage.department == departments[0]:
            i += 1
        if stage.department == departments[1]:
            j += 1

    # process the POST-request and write to database
    if request.method == "POST":

        all_answers = []
        for answer in answers:

            if request.POST.get('set_like_' + str(answer.question_id)):
                answer.like = request.POST.get('set_like_' + str(answer.question_id))
                answer.date = datetime.date.today()
            if request.POST.get('set_grade_' + str(answer.question_id)):
                answer.grade_id = int(request.POST.get('set_grade_' + str(answer.question_id)))
                answer.date = datetime.date.today()
            all_answers.append(answer)

        bulk_update(answers)
        answers = AnswerModel.objects.filter(user=user_id)
        auth.logout(request)
        return redirect('home')

    return render(request, "formapp/table.html", context={'questions':questions, 'stages':stages, 'departments':departments, 'answers':answers, 'grades':grades, 'user_name':user_name})



