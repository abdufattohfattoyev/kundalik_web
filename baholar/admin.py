from django.contrib import admin

from .models import Subject,Grade,Student

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Grade)


