from django.contrib import admin
from .models import *
# Register your models here.


class CaseAdmin(admin.ModelAdmin):
    list_display = ['id', 'fname', 'lname', 'program']

    class Meta:
        model = t_case


admin.site.register(t_case, CaseAdmin)
