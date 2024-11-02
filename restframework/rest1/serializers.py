from rest_framework import serializers
from rest1.models import *
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20)
    age=serializers.IntegerField()
    usn=serializers.CharField(max_length=20)
    address=serializers.CharField()
    date=serializers.DateField()
    def create(self, validated_data):
        return StudentModels.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.age=validated_data.get('age',instance.age)
        instance.save()
        return instance