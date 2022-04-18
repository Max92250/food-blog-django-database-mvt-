from django.contrib import admin

# Register your models here.
from myapp.models import Contact,Employee


admin.site.register(Contact)
admin.site.register(Employee)