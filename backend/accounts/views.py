from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate
# Create your views here.

class UserView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        s = UserSerializer(data = request.data)
        if s.is_valid():
            user = s.save()
            return Response({
                "message": "User registered successfully",
            },status=status.HTTP_201_CREATED)
        return Response(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):
    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({"error":"Email and password required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(request,email=email,password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "access": str(refresh.access_token),
                "refresh": str(refresh),
                "email": user.email,
                "user_name": user.user_name,
                "role": user.role
            }, status=status.HTTP_200_OK)
        return Response({"Error":"Invalid Credentials"},status=status.HTTP_401_UNAUTHORIZED)
    