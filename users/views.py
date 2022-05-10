from rest_framework import generics, permissions, views
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from .permission import IsOwnerOrReadOnly


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    lookup_field = 'username'

    def get_queryset(self):
        return User.objects.all()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class LogoutUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        request.user.auth_token.delete()

        return Response('You Logged out successfully.', status=200)
