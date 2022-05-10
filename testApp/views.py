from rest_framework.response import Response
from .serializers import QuizSerializer, QuestionSerializer, AnswerSerializer, UserAnswerSerializer
from rest_framework import generics, permissions, status
from .models import Quiz, Question, Answer, MarksOfUser
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.exceptions import NotAcceptable, NotFound


class QuizListView(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class QuizCreateView(generics.CreateAPIView):
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAdminUser]


class QuizDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuizSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    queryset = Quiz.objects.all()


class QuestionListCreateView(generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        quiz = get_object_or_404(Quiz, id=self.kwargs.get('quiz_id'))
        return Question.objects.filter(quiz=quiz)

    def perform_create(self, serializer):
        quiz = get_object_or_404(Quiz, id=self.kwargs['quiz_id'])
        serializer.save(quiz=quiz)


class AnswerCreateView(generics.ListCreateAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        question = get_object_or_404(Question, id=self.kwargs.get('quest_id'))
        return Answer.objects.filter(question=question)

    def perform_create(self, serializer):
        question = get_object_or_404(Question, id=self.kwargs['quest_id'])
        serializer.save(question=question)


class AnswerToQuestionView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        question = get_object_or_404(Question, id=self.kwargs.get('question_id'))

        if MarksOfUser.objects.filter(question=question, user=request.user, quiz=question.quiz).exists():
            raise NotAcceptable('you already answered to this question')

        serializer = UserAnswerSerializer(data=request.data)

        if serializer.is_valid():

            try:
                correct_answer = question.answer_set.get(is_correct=True)
            except Answer.DoesNotExist as e:
                raise NotFound(e)

            quiz = question.quiz

            marks, _ = MarksOfUser.objects.get_or_create(quiz=quiz, user=request.user)
            marks.question.add(question)

            if correct_answer.number == serializer.validated_data['user_answer']:
                request.user.point += 10
                request.user.save()
                return Response({'message': 'answer is correct.'}, status.HTTP_200_OK)

            else:
                return Response({'message': 'answer is wrong! try harder.'}, status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
