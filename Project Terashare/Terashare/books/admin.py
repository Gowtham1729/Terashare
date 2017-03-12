from django.contrib import admin
from .models import Course, File, Folder, Profile

admin.site.register(Course)
admin.site.register(Folder)
admin.site.register(Profile)
admin.site.register(File)
