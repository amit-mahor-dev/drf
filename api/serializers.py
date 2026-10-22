from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import student, book

class student_serialzer(ModelSerializer):
    # student_name = serializers.CharField(source = "name")
    # sehar = serializers.CharField(source = "city")
    class Meta:
        model = student
        # fields = ["sehar","state","student_name","id", "name"]
        fields = "__all__" 
        
        
class book_ser(serializers.ModelSerializer):
    students = student_serialzer(source = "student")
    class Meta:
        model = book
        fields = "__all__"