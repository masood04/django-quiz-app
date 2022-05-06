from .serializers import QuizSerializer
from rest_framework import generics, permissions
from .models import Quiz


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



