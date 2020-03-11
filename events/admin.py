from django.contrib import admin
from .models import Conference, Person, Company
# Register your models here.
admin.site.register(Conference)
admin.site.register(Person)
admin.site.register(Company)
