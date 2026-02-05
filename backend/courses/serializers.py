from rest_framework import serializers
from .models import Chapter, Course, Section, UserCourses

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['id', 'title', 'video_url', 'video_duration', 'order']


class SectionSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'order', 'chapters']


class CourseSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'thumbnail', 'total_hours', 'language', 'created_at', 'is_published', 'creator', 'sections']
        read_only_fields = ['id', 'creator', 'created_at']

class EnrollmentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserCourses
        fields = ['id', 'user', 'course', 'enrolled_on', 'is_completed']
        read_only_fields = ['id', 'enrolled_on']