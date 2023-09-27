from django.contrib import admin
from .models import Institute, Teacher, Review, Department, InstitutePhoto, TeacherPhoto

admin.site.register(Institute)
admin.site.register(Teacher)
admin.site.register(Review)
admin.site.register(Department)
admin.site.register(InstitutePhoto)
admin.site.register(TeacherPhoto)
