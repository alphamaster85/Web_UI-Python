from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from formapp.models import AnswerModel, QuestionModel
from authapp.models import UserDataModel, RoleModel

# check whether there are records in the database for one user
# if not, create new response records
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

# main function view of authaap
def index(request):

    if request.method == "POST":

        user = auth.authenticate(username=request.POST.get('log'), password=request.POST.get('pass'))
        if user is not None:
            auth.login(request, user)
            role = UserDataModel.objects.get(user_id=user.id).name
            id = UserDataModel.objects.get(user_id=user.id).user_id

            if is_not_emty(user):
                if id == 1:
                    return redirect('{}/'.format(role.lower()))
                return redirect('form/{}'.format(id))

    return render(request, "authapp/first.html", context={})