from django.urls import path
from . import views


urlpatterns = [
    path('quiz', views.QuizListView.as_view(), name='quiz-list'),
    path('quiz/create', views.QuizCreateView.as_view(), name='quiz-create'),
    path('quiz/<int:pk>/', views.QuizDetailView.as_view(), name='quiz-detail'),
    path('quiz/<int:quiz_id>/question', views.QuestionCreateView.as_view(), name='question-create'),
    path('question/<int:quest_id>/answer', views.AnswerCreateView.as_view(), name='answer-create'),

]
