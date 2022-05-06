from django.urls import path
from . import views


urlpatterns = [
    path('quiz', views.QuizListView.as_view(), name='quiz-list'),
    path('quiz/create', views.QuizCreateView.as_view(), name='quiz-create'),
    path('quiz/<int:pk>/', views.QuizDetailView.as_view(), name='quiz-detail')
]
