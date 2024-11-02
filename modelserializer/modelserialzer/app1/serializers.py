from rest_framework import serializers
from app1.models import StudentModel
class StudentSerializer(serializers.ModelSerializer):
    # roll=serializers.CharField(read_only=True)
    class Meta:
        model=StudentModel
        fields='__all__'
        read_only=['name','roll']