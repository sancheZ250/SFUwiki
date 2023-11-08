from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Institute(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    abbreviation = models.CharField(max_length=10)
    logo = models.ImageField(upload_to='institute_logos', null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.abbreviation})'


class InstitutePhoto(models.Model):
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='institute_photos')

    def __str__(self):
        return f'Фотография {self.institute.abbreviation}а'


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    institute = models.ForeignKey(Institute, null=True, blank=False, on_delete=models.SET_NULL,
                                  related_name='departments')
    logo = models.ImageField(upload_to='department_logos', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Teacher(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.SET_NULL,related_name='teachers')
    alma_mater = models.CharField(max_length=100)
    bio = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=1)
    knowledge_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    teaching_skill_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    easiness_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    communication_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    avg_rating = models.DecimalField(max_digits=4, decimal_places=3, default=0)
    institute = models.ForeignKey(Institute, null=True, blank=True, on_delete=models.SET_NULL, related_name='teachers')
    review_count = models.PositiveIntegerField(default=0)
    date_published = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    first_photo = models.ImageField(upload_to='teachers_first_photos', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-avg_rating']


rating_validator = [MinValueValidator(1), MaxValueValidator(5)]


class TeacherPhoto(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='teachers_photo')

    def __str__(self):
        return f'{self.pk} фото преподавателя {self.teacher}'


class Review(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    knowledge_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    teaching_skill_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    easiness_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    communication_rating = models.PositiveSmallIntegerField(validators=rating_validator)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)

    def __str__(self):
        return f"{'Anonymous' if self.is_anonymous else self.student.username}: {self.comment}"


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField(Teacher, related_name='disciplines', blank=True)

    def __str__(self):
        return self.name
