from django.urls import path, include
from .views import UserView, LoginView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path('register/',UserView.as_view()),
    path('login/',LoginView.as_view()),
    path('refresh/',TokenRefreshView.as_view()),
    path('auth/', include('rest_framework.urls')),
]


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcwMzY3ODU2LCJpYXQiOjE3NzAyODE0NTYsImp0aSI6IjM2ZWY0OTk5NzAyZTQxNzhiMmZmYjUyM2Q2Y2JlOGY5IiwidXNlcl9pZCI6IjEifQ.KZmMoSTXun0rfCAy1qDh93Ky2Zvf642V1wFmLpWzoyg
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc3MDg4NjI1NiwiaWF0IjoxNzcwMjgxNDU2LCJqdGkiOiI3YzcyM2I5NjhlMTk0ZTBhYTcyMDg3ZDg3OTkxNTMyMiIsInVzZXJfaWQiOiIxIn0.BDOo1-POY7vaB19H26tlhjoV3j4HMTjGWchcMBdR7uM