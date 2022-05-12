# Importo los modelos:
from apps.leads.models import Student, Career, Course

from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ('__all__',)


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('__all__',)


class CareerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Career
        fields = ('__all__',)