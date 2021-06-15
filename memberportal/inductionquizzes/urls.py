from django.urls import path
from . import views

urlpatterns = [
    path("api/quiz/",views.Inductionquiz.as_view(), name="induction_quizzes"),
    path("api/quiz/submission/",views.QuizSubmission.as_view(), name="QuizSubmission"),
]
