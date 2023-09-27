from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Institute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    abbreviation = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'


class InstitutePhoto(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='institute_photos')

    def __str__(self):
        return f'Фотография {self.institute.abbreviation}а'


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    institute = models.ForeignKey(Institute, null=True, blank=False, on_delete=models.SET_NULL,
                                  related_name='departments')

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL)
    alma_mater = models.CharField(max_length=100)
    bio = models.TextField()
    knowledge_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    teaching_skill_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    easiness_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    communication_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    institute = models.ForeignKey(Institute, null=True, blank=True, on_delete=models.SET_NULL, related_name='teachers')

    def __str__(self):
        return self.name


rating_validator = [MinValueValidator(1), MaxValueValidator(5)]


class TeacherPhoto(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='teachers_photo')

    def __str__(self):
        return f'{self.pk} фото преподавателя {self.teacher.name}'


class Review(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    knowledge_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    teaching_skill_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    easiness_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    communication_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"{'Anonymous' if self.is_anonymous else self.student.username}: {self.comment}"
