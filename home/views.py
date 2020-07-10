from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def introduction(request):
  return render(request, "home/html/Introduction.html")

def theory(request):
  return render(request, "home/html/Theory.html")

def objective(request):
  return render(request, "home/html/Objective.html")

def manual(request):
  return render(request, "home/html/Manual.html")

def procedure(request):
  return render(request, "home/html/Procedure.html")

def further_readings(request):
  return render(request, "home/html/Further Readings.html")

def feedback(request):
  return render(request, "home/html/Feedback.html")

def experiments(request):
  return render(request, "home/html/Experiment.html")

def quizzes(request):
  return render(request, "home/html/Quizzes.html")
