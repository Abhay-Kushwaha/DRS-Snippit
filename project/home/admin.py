from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.site_header = "Employee Management"
admin.site.site_title = "Employee Management Portal"
admin.site.register(Caste)