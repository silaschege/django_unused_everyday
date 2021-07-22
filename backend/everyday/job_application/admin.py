from django.contrib import admin

# Register your models here.
from .models import Applicant,Guarantors,Business_job_application,Job_listing
admin.site.register (Applicant)
admin.site.register (Guarantors)
admin.site.register (Business_job_application)
admin.site.register (Job_listing)