from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404

from courses.models import Chapter, Course, Section

from courses.serializers import CourseSerializer, SectionSerializer, ChapterSerializer

from courses.permissions import IsCreator

class CourseListCreateView(APIView):
    def get(self, request):
        courses = Course.objects.filter(is_published=True)
        s = CourseSerializer(courses, many = True)
        return Response(s.data)
    
    def post(self, request):
        self.permission_classes = [IsAuthenticated, IsCreator]
        s = CourseSerializer(data = request.data)
        if s.is_valid():
            s.save(creator = request.user)
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CourseDetailView(APIView):

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsCreator()]
    
    def get_object(self, pk):
        return get_object_or_404(Course, pk=pk)

    def get(self,request,pk):
        course = self.get_object(pk)
        s = CourseSerializer(course)
        return Response(s.data)
    
    def patch(self, request, pk):
        course = self.get_object(pk)

        if course.creator != request.user:
            return Response({"error": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        
        s = CourseSerializer(course, data = request.data, partial = True)

        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        course = self.get_object(pk)
        if course.creator != request.user:
            return Response({"error": "Forbidden"}, status=status.HTTP_403_FORBIDDEN)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class SectionCreateView(APIView):
    permission_classes = [IsAuthenticated,IsCreator]

    def post(self, request):
        s = SectionSerializer(data = request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)

class ChapterCreateView(APIView):
    
    permission_classes = [IsAuthenticated, IsCreator]

    def post(self, request):
        s = ChapterSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=status.HTTP_201_CREATED)
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
