from .views import (
                    Applicant_viewset,
                    Guarantors_viewset,
                    Business_job_application_viewset,
                    Job_listing_viewset,
                    )
from django.urls import path
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'Applicant',Applicant_viewset, basename='Applicant')
router.register(r'Guarantors',Guarantors_viewset, basename='Guarantors')
router.register(r'Business_application',Business_job_application_viewset, basename='Business_job_application')
router.register(r'Listing',Job_listing_viewset, basename='Job_listing')
urlpatterns = router.urls