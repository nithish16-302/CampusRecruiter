from django.contrib import admin

# Register your models here.
from .models import Recruitment
from .models import Students

admin.site.register(Recruitment)
admin.site.register(Students)