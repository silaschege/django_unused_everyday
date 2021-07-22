import uuid
from django.db import models



# Create your models here.

class Business_hr_management(models.Model):
    Business_Id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Business_Name   =   models.TextField()
    Phone_Number    =   models.TextField()
    Industry    =   models.TextField()
    Email   =   models.EmailField()
    Director_First_Name =   models.TextField()
    Directors_Last_Name =   models.TextField()
    Directors_Other_Name    =   models.TextField()
    Directors_Phone_Number  =   models.TextField()
    Director_Email  = models.EmailField()

class Employee(models.Model):
    Employee_Id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_name  =   models.TextField()  
    Last_name   =   models.TextField() 
    Other_Names =   models.TextField()
    Id_Number   =   models.TextField()
    Phone_Number    =   models.TextField()
    Post    =   models.TextField()
    Company_Position    =   models.TextField()
    Business_hr_management    =   models.ForeignKey(Business_hr_management,on_delete=models.CASCADE)

class Work_day(models.Model):
    Work_day_id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Date    =   models.DateField()
    Business_hr_management    =   models.ForeignKey(Business_hr_management,on_delete=models.CASCADE)
    Employee =  models.ManyToManyField(Employee)

class Announcement(models.Model):
    Communication_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Message =   models.TextField()
    From    =   models.TextField()
    To  =   models.TextField()
    Business_hr_management    =   models.ForeignKey(Business_hr_management,on_delete=models.CASCADE)
    Employee    =   models.ForeignKey(Employee,on_delete=models.CASCADE)

class Issue(models.Model):
    Issue_Id    =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Staff_issue =   models.TextField()
    Date    =   models.DateField()
    Disciplinary_Action =   models.TextField()
    Action_Taken    =   models.TextField()
    Business_hr_management    =   models.ForeignKey(Business_hr_management,on_delete=models.CASCADE)
    Employee    =   models.ForeignKey(Employee,on_delete=models.CASCADE)

class Complain(models.Model):
    Complain_Id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Staff_issue =   models.TextField()
    Date    =   models.DateField()
    Disciplinary_Action =   models.TextField()
    Action_Taken    =   models.TextField()
    Business_hr_management    =   models.ForeignKey(Business_hr_management,on_delete=models.CASCADE)
    Employee    =   models.ForeignKey(Employee,on_delete=models.CASCADE)

class Task (models.Model):
    Task_id =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Task    =   models.TextField()
    State   =   models.BooleanField()
    From    =   models.TextField()
    Date    =   models.DateField()
    Business_hr_management    =   models.ForeignKey(Business_hr_management,on_delete=models.CASCADE)
    Employee =  models.ManyToManyField(Employee)


