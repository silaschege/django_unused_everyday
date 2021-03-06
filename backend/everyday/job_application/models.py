import uuid
from django.db import models

# Create your models here.
class Applicant (models.Model):
    Applicant_Id    =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_name   =   models.TextField()
    Last_name   =   models.TextField()
    Other_Names   =   models.TextField()
    Email   =   models.EmailField()
    Date_of_birth   =   models.DateField()
    Id_Number   =   models.TextField()
    Phone_Number   =   models.TextField()
    Level_of_Education   =   models.TextField()
    Course   =   models.TextField()
    Other_Education   =   models.TextField()
    Previous_Job   =   models.TextField()
    Time_Worked_There   =   models.IntegerField()

class Guarantors (models.Model):
    Guarantors_Id   =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    First_name   =   models.TextField()
    Last_name   =   models.TextField()
    Other_Names   =   models.TextField()
    Email   =   models.EmailField()
    Id_Number   =   models.TextField()
    Phone_Number   =   models.TextField()
    Relationship   =   models.TextField()   
    Applicant   =   models.ForeignKey(Applicant,on_delete=models.CASCADE)

class Business_job_application  (models.Model):
    Business_Id   =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Business_name   =   models.TextField()
    

class  Job_listing (models.Model):
    Job_listing_Id   =   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Education_level   =   models.TextField()
    Course   =   models.TextField()
    Years_experience    =   models.IntegerField()
    End_of_application_date =   models.DateField()
    Position   =   models.TextField()
    Location   =   models.TextField()
    Applicant   =   models.ManyToManyField(Applicant)
    Business_job_application    =   models.ForeignKey(Business_job_application,on_delete=models.CASCADE)