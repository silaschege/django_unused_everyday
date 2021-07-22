from rest_framework import serializers
from job_application.models import (
                    Applicant,
                    Guarantors,
                    Business_job_application,
                    Job_listing,
                    )


class Applicant_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Applicant
        fields  =   '__all__'

class Guarantors_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Guarantors
        fields  =   '__all__'

class Business_job_application_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Business_job_application
        fields  =   '__all__'

class Job_listing_Serializer(serializers.ModelSerializer):
    class Meta:
        model   =   Job_listing
        fields  =   '__all__'


