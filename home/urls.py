from django.urls import path

from . import views

urlpatterns = [
    path('', views.introduction, name="introduction"),
    path('theory', views.theory, name="theory"),
    path('objective', views.objective, name="objective"),
    path('manual', views.manual, name="manual"),
    path('procedure', views.procedure, name="procedure"),
    path('further_readings', views.further_readings, name="further_readings"),
    path('feedback', views.feedback, name="feedback"),
    path('experiments', views.experiments, name="experiment"),
    path('quizzes', views.quizzes, name="quizzes"),
]
