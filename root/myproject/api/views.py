from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Profile,Vacancy,Vacancy_Record
from .serializers import Profile_Serializer,Vacancy_Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.PermissionDenied
from rest_framework.response import Response
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


class VacancyViewSet(ModelViewSet):
	queryset=Vacancy.objects.all()
	serializer_class=Vacancy_Serializer

	
	def perform_create(self,serializer):
		if request.user.profile.role =='student':
			serializer=self.get_serializer(data=request.data)

			serializer.save(posted_by=self.request.user)

		else:
			raise PermissionDenied('only student can create vacancy')
		   

    @action(detail=True,methods=['post'])
    def book(self,request,pk=None):
    	if request.user.profile.role=='teacher':
    		user=self.request.user
    		record=user.teacher_record.filter(is_active=True).count()
    		if record<3:
    		  vacancy=self.get_object()
    		  teacher=self.request.user
    		  student=vacancy.profile.user

    		  Vacancy_Record.objects.create(vacancy=vacancy,teacher=teacher,student=student)
    		  vacancy.status='closed'
    		  vacancy.assigned_to=teacher
    		  vacancy.save()

    		  return Response({'message':'Booked successfully'})
            else:
            	raise PermissionDenied("You cannot tech more than two tutuion")



        else:
        
          raise PermissionDenied("only teacher can book a vacancy")	







		





		 

