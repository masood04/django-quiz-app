from rest_framework.response import Response

from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer
from rest_framework import generics, permissions
from .models import Quiz, Question
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView


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


class QuestionListCreateView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs.get('quiz_id'))
        return Question.objects.filter(quiz=quiz)

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


class AnswerToQuestionView(APIView):

    def post(self, request, *args, **kwargs):

        serializer = UserAnswerSerializer(data=request.data)

        if serializer.is_valid():
            question = get_object_or_404(Question, id=self.kwargs.get('question_id'))
            correct_answer = question.answer_set.get(is_correct=True)

            if correct_answer.number == serializer.validated_data['user_answer']:
                # request.user.point += 10

                return Response({'message': 'answer was correct.'}, status=200)
            else:
                return Response({'message': 'answer was wrong! try harder.'}, status=200)

        else:
            return Response(serializer.errors)
