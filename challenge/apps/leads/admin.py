from django.contrib import admin

from apps.leads.models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    pass