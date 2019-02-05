from django.http import HttpResponse
from django.shortcuts import render
from .models import StageModel, QuestionModel, AnswerModel, GradeModel

def index(request):
    USER_ID = 1

    stages = StageModel.objects.all()
    questions = QuestionModel.objects.all()
    departments = ['Activities', 'Skills']  # list(set(StageModel.objects.all()))
    answers = AnswerModel.objects.filter(user_id=USER_ID)
    grades = GradeModel.objects.all()

    if request.method == "POST":

        all_answers = []
        for answer in answers:
            if request.POST.get('set_like_' + str(answer.question_id)):
                answer.like = request.POST.get('set_like_' + str(answer.question_id))
            if request.POST.get('set_grade_' + str(answer.question_id)):
                answer.grade_id = int(request.POST.get('set_grade_' + str(answer.question_id)))
            all_answers.append(answer)
            answer.save()

        # AnswerModel.objects.bulk_create(all_answers)

        answers = AnswerModel.objects.filter(user=USER_ID)

    return render(request, "formapp/formapp.html", context={'questions':questions, 'stages':stages, 'departments':departments, 'answers':answers, 'grades':grades})