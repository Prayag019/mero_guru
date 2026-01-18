from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator






class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    role=models.CharField(max_length=20,choices=[('teacher','Teacher'),('student','Student')],default='student')
    full_name=models.CharField(max_length=100)
    permanant_address=models.CharField(max_length=100)
    current_address=models.CharField(max_length=100)
    age=models.IntegerField()
    verified=models.BooleanField(default=False)



class Qualification(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    highschool_status = models.CharField( max_length=10, choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending')
    highschool_institution = models.CharField(max_length=255, blank=True, null=True)
    bachelor_status = models.CharField( max_length=10, choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending' )
    bachelor_institution = models.CharField(max_length=255, blank=True, null=True)
    master_status = models.CharField( max_length=10, choices=[('completed', 'Completed'), ('pending', 'Pending')], default='pending' )
    master_institution = models.CharField(max_length=255, blank=True, null=True)



class Vacancy(models.Model):
    posted_by=models.ForeignKey(Profile,on_delete=models.CASCADE,default=None)
    vacancy_type=models.CharField(max_length=50,choices=[('tution_teacher','Tution_Teacher'),('school_teacher','School_teacher')],default='tution_teacher')
    status=models.CharField(max_length=25,default='open',choices=[('open','Open'),('closed','Closed')])
    grade=models.IntegerField()
    salary=models.IntegerField()
    location=models.CharField(max_length=100)
    description=models.TextField()
    assigned_to=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default=None)




class Tutuor_Booking_Counter(models.Model):
    
    teacher=models.ForeignKey(User,on_delete=models.CASCADE)


class Vacancy_record(models.model):
    vacancy=models.OneToOneField(Vacancy,on_delete=models.CASCADE)
    teacher=models.ForeignKey(User,on_delete=models.CASCADE,related_name='teacher_record')
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name='student_record') 
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_add_now=True)







    






