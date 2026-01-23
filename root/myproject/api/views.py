from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Profile,Vacancy,Vacancy_record,Application_Record
from .serializers import Profile_Serializer,Vacancy_Serializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django.core.exceptions import PermissionDenied
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
      if self.request.user.profile.role=='teacher':
        user=self.request.user
        record=user.teacher_record.filter(is_active=True).count()
        if record<3:
          vacancy=self.get_object()
          teacher=self.request.user
          student=vacancy.posted_by.user

          Vacancy_record.objects.create(vacancy=vacancy,teacher=teacher,student=student)
          vacancy.status='closed'
          vacancy.assigned_to=teacher
          vacancy.save()

          return Response({'message':'Booked successfully'})
        else:
              raise PermissionDenied("You cannot tech more than two tutuion")



      else:
        
          raise PermissionDenied("only teacher can book a vacancy") 


  @action(detail=True,methods=['post'])     
  def apply(self,request,pk=None):
    if self.request.user.profile.role=='teacher':
      if self.request.user.teacher_record.count()<3:
        vacancy=self.get_object()
        teacher=self.request.user
        student=vacancy.posted_by.user 

        if Application_Record.objects.get(teacher=teacher).exists():
          return Response("you have already applied")
        else:
          
          Application_Record.objects.create(teacher=teacher,vacancy=vacancy)

          return Response("Applied successfully")

  
  @action(detail=True,methods=['post'])
  def accept(self,request,pk=None):
    vacancy=self.get_object()
    teacher = vacancy.application.teacher 
    student=self.request.user 
    Vacancy_record.objects.create(vacancy=vacancy,teacher=teacher,student=student)
    vacancy.is_active=False
    return Response("You have succesfully accepted the teacher")


  @action(detail=True,methods=['post'])
  
  def end_vacancy(self,request,pk=None):
    vacancy=self.get_object()

    if self.request.user.profile.role=='teacher' && self.request.user.profile.verified=='True':
      if vacancy.vacancy_record.teacher== self.request.user
        vacancy.delete()
        return Response('Vacancy ended successfully')

      else:
         return Response('cannot perform the action')  



    else:
        if vacancy.vacancy_record.student==self.request.user:
          vacancy.delete()
          return Response('Vacancy ended successfully')

         else:
         return Response('cannot perform the action')   





       






       

      

       







    





      













   









class ProfileViewSet(ModelViewSet):
      queryset=Profile.objects.all()
      serializer_class=Profile_Serializer


      def perform_create(self,serializer):

          serializer.save(user=self.request.user) 











    





     

