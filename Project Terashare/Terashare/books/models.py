import os
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Course(models.Model):
    course_title = models.CharField(max_length=5)
    course_code = models.CharField(max_length=3)

    def __str__(self):
        return self.course_title + ' - ' + self.course_code


class Folder(models.Model):
    folder = models.CharField(max_length=99)

    def __str__(self):
        return self.folder


class File(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    file_type = models.ForeignKey(Folder)
    file_name = models.CharField(max_length=255)
    file_path = models.FileField(max_length=255)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('books:files', kwargs={'course_id':self.course.id, 'folder_id': self.file_type.id })

    def __str__(self):
        return self.file_name

    def filename(self):
        return os.path.basename(self.file_path.name)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=8)
    Programmes = (('Btech', 'Btech'), ('Mtech', 'Mtech'), ('Msc', 'Msc'), ('Ma', 'Ma'), ('Phd', 'Phd'), ('Alumni', 'Alumni'))
    programme = models.CharField(max_length=5, default='Btech', choices=Programmes)

    def __str__(self):
        return self.user.username
