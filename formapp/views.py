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

    i = 1; j = 1
    stage_indexes = {}
    for stage in stages:
        if stage.department == departments[0]:
            stage_indexes[stage.id] = i
            i += 1
        if stage.department == departments[1]:
            stage_indexes[stage.id] = j
            j += 1
        print(stage_indexes[stage.id])

    if request.method == "POST":

        all_answers = []
        for answer in answers:

            ans = AnswerModel()
            ans.id = answer.id
            ans.question_id = answer.question_id
            ans.user_id = answer.user_id

            print(ans.user_id, ans.question_id, ans.id)
            if request.POST.get('set_like_' + str(answer.question_id)):
                ans.like = request.POST.get('set_like_' + str(answer.question_id))
            if request.POST.get('set_grade_' + str(answer.question_id)):
                ans.grade_id = int(request.POST.get('set_grade_' + str(answer.question_id)))
            all_answers.append(ans)
            # answer.save()

        AnswerModel.objects.bulk_create(all_answers)

        # answers = AnswerModel.objects.filter(user=USER_ID)

    return render(request, "formapp/formapp.html", context={'questions':questions, 'stages':stages, 'departments':departments, 'answers':answers, 'grades':grades, 'stage_indexes':stage_indexes})