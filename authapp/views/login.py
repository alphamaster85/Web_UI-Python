from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from authapp.models import UserModel, UserDataModel
from formapp.models import AnswerModel, QuestionModel

def is_valid(user, log_pass):
    if user.login == log_pass[0]:
        if user.password == log_pass[1]:
            return True

def is_not_emty(user):
    answers = AnswerModel.objects.filter(user_id=user.id)
    questions = QuestionModel.objects.all()
    if len(answers) == 0:

        all_answers = []
        for question in questions:
            answer = AnswerModel()
            answer.user_id = user.id
            answer.question_id = question.id
            all_answers.append(answer)

        AnswerModel.objects.bulk_create(all_answers)
    return True

def index(request):

    if request.method == "POST":

        users = UserModel.objects.all()
        for user in users:
            log_pass = []
            if request.POST.get('log'):
                log_pass.append(request.POST.get('log'))
                if request.POST.get('pass'):
                    log_pass.append(request.POST.get('pass'))
            if is_valid(user, log_pass):
                if is_not_emty(user):
                    return redirect('form/{}'.format(user.id))


    return render(request, "authapp/first.html", context={})