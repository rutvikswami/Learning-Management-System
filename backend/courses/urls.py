from django.urls import path
from .view_list.course_views import ChapterCreateView, ChapterDetailView, SectionCreateView, SectionDetailView, CourseListCreateView, CourseDetailView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name = 'course-list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name = 'course-detail'),

    path('sections/', SectionCreateView.as_view(), name = 'section-list'),
    path('sections/<int:pk>/', SectionDetailView.as_view(), name = 'section-detail'),

    path('chapters/', ChapterCreateView.as_view(), name = 'chapter-list'),
    path('chapters/<int:pk>/', ChapterDetailView.as_view(), name = 'chapter-detail'), 
]
