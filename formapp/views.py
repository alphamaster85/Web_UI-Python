from django.http import HttpResponse
from django.shortcuts import render
from .models import StageModel, QuestionModel

# def index(request):
#     return HttpResponse("Hello World!")

def index(request):

    stages = StageModel.objects.all()
    questions = QuestionModel.objects.all()
    departments = ['Activities', 'Skills'] # list(set(StageModel.objects.all()))

    return render(request, "formapp/formapp.html", context={'questions':questions, 'stages':stages, 'departments':departments})