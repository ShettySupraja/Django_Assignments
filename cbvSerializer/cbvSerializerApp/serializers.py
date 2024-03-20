from typing import __all__
from rest_framework import serializers
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'rating']
        # or fields = __all__ will return all the fields in the model