from django.contrib import admin

# Register your models here.
from .models import (
                    Business_hr_management,
                    Employee,
                    Work_day,
                    Complain,
                    Announcement,
                    Issue,
                    Task
                    )

admin.site.register (Business_hr_management)
admin.site.register (Employee)
admin.site.register (Work_day)
admin.site.register(Complain)
admin.site.register (Announcement)
admin.site.register (Issue)
admin.site.register (Task)
                     



