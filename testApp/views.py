from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer
from rest_framework import generics, permissions
from .models import Quiz, Question
from django.shortcuts import get_object_or_404


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuizCreateView(generics.CreateAPIView):
    serializer_class = QuizSerializer
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    # permission_classes = [permissions.IsAdminUser]
    queryset = Quiz.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class QuestionCreateView(generics.CreateAPIView):
    serializer_class = QuestionSerializer

    def perform_create(self, serializer):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_id'])
        serializer.save(quiz=quiz)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerSerializer

    def perform_create(self, serializer):
        question = get_object_or_404(Question, id=self.kwargs['quest_id'])
        serializer.save(question=question)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
