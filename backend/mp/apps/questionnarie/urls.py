from django.urls import path
from . import views

app_name = 'questionnarie'

urlpatterns = [
    path('make/', views.QuestionnaireView.as_view(), name='make'),
]