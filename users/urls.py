from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token as auth_views
from . import views

urlpatterns = [
    path('login', auth_views, name='login'),
    path('user/<slug:username>/', views.UserDetailView.as_view(), name='user-detail'),
    path('user/create', views.UserCreateView.as_view(), name='user-create'),
    path('logout', views.LogoutUserView.as_view(), name='logout'),

]
