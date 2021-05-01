from django.urls import path
from . import views

urlpatterns = [
    path(
        "api/quiz/",
        views.Inductionquiz.as_view(),
        name="induction_quizzes",
    )
]
