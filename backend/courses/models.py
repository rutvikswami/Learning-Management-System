from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Course(models.Model):
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='created_courses'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(
        upload_to='course_thumbnails/',
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Sections(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='sections'
    )
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"
    
class Chapters(models.Model):
    chapter = models.ForeignKey(
        Sections,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"
class UserCourses(models.Model):
    user_id=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="accounts"
    )
    course_id=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_name"
    )
    enrolled_on=models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user_id}. {self.course_id}"
