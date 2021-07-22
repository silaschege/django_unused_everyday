from hr_management.models import (
                    Business_hr_management,
                    Employee,
                    Work_day,
                    Complain,
                    Announcement,
                    Issue,
                    Task
                    )
from .serializers import (
                    Business_hr_management_Serializer,
                    Employee_Serializer,
                    Work_day_Serializer,
                    Complain_Serializer,
                    Announcement_Serializer,
                    Issue_Serializer,
                    Task_Serializer
                    )
from rest_framework import viewsets

class Business_hr_management_viewset(viewsets.ModelViewSet):
    serializer_class    =   Business_hr_management_Serializer
    queryset    =   Business_hr_management.objects.all()

class Employee_viewset(viewsets.ModelViewSet):
    serializer_class    =   Employee_Serializer
    queryset    =   Employee.objects.all()

class Work_day_viewset(viewsets.ModelViewSet):
    serializer_class    =   Work_day_Serializer
    queryset    =   Work_day.objects.all()

class Complain_viewset(viewsets.ModelViewSet):
    serializer_class    =   Complain_Serializer
    queryset    =   Complain.objects.all()

class Announcement_viewset(viewsets.ModelViewSet):
    serializer_class    =   Announcement_Serializer
    queryset    =   Announcement.objects.all()

class Issue_viewset(viewsets.ModelViewSet):
    serializer_class    =   Issue_Serializer
    queryset    =   Issue.objects.all()

class Task_viewset(viewsets.ModelViewSet):
    serializer_class    =   Task_Serializer
    queryset    =   Task.objects.all()