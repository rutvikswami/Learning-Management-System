from django.db import models
from django.conf import settings
from django.db.models import F
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
    total_hours = models.FloatField(default=0.0)
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def calculate_total_hours(self):
        total_minutes = Chapter.objects.filter(
            section__course=self
        ).aggregate(total = sum('video_duration'))['total'] or 0

        return round(total_minutes/60)
    
    def save(self, *args, **kwargs):
        self.total_hours = self.calculate_total_hours()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Section(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='sections'
    )
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ['course','order']

    def save(self, *args, **kwargs):
        if not self.pk:
            Section.objects.filter(
                course = self.course,
                order__gte = self.order
            ).update(order = F('order') + 1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order}. {self.title}"
    

class Chapter(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.CASCADE,
        related_name='chapters'
    )
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    video_duration = models.FloatField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ['section','order']

    def save(self, *args, **kwargs):
        if not self.pk:
            Chapter.objects.filter(
                section = self.section,
                order__gte = self.order
            ).update(order = F('order') + 1)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.order}. {self.title}"
    

class UserCourses(models.Model):
    user=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_name"
    )
    enrolled_on=models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['user','course']

    def __str__(self):
        return f"{self.user}. {self.course}"
