from job_application.models import (
                    Applicant,
                    Guarantors,
                    Business_job_application,
                    Job_listing,
                    )
from .serializers import (
                    Applicant_Serializer,
                    Guarantors_Serializer,
                    Business_job_application_Serializer,
                    Job_listing_Serializer
                    )
from rest_framework import viewsets

class Applicant_viewset(viewsets.ModelViewSet):
    serializer_class    =   Applicant_Serializer
    queryset    =   Applicant.objects.all()

class Guarantors_viewset(viewsets.ModelViewSet):
    serializer_class    =   Guarantors_Serializer
    queryset    =   Guarantors.objects.all()

class Business_job_application_viewset(viewsets.ModelViewSet):
    serializer_class    =   Business_job_application
    queryset    =   Business_job_application.objects.all()

class Job_listing_viewset(viewsets.ModelViewSet):
    serializer_class    =   Job_listing_Serializer
    queryset    =   Job_listing.objects.all()

