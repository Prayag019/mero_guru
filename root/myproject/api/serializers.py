from rest_framework import serializers
from .models import Vacancy,Profile,Qualification


class Vacancy_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Vacancy
		exclude=['posted_by','status','assigned_to']

class Profile_Serializer(serializers.ModelSerializer):
	class Meta:
		model=Profile
		exclude=['user','verified']

class Qualification_Serializer(serializers.ModelSerializer):
    class Meta:
        model=Qualification
        exclude=['user']


        		

