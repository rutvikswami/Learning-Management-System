from django.contrib import admin
from .models import Chapter, Course, UserCourses, Section
# Register your models here.
admin.site.register(Chapter)
admin.site.register(Course)
admin.site.register(UserCourses)
admin.site.register(Section)