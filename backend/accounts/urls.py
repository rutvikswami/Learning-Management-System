from django.urls import path
from .views import UserView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    ('register/',UserView.as_view()),
    ('login/',LoginView.as_view()),
    ('refresh/',TokenRefreshView.as_view()),
]
