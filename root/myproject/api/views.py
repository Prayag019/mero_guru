from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Profile,Vacancy
from .serializers import Profile_Serializer,Vacancy_Serializer


class Create_Profile_API(ListCreateAPIView):
	queryset=Profile.objects.all()
	serializer_class=Profile_Serializer


	def perform_create(self,serializer):
		serializer.save(user=self.request.user)



class Post_Vacancy_Api(ListCreateAPIView):

	queryset=Vacancy.objects.all()
	serializer_class=Vacancy_Serializer


	def perform_create(self,serializer):

		serializer.save(created_by=self.request.user)
		





		 

