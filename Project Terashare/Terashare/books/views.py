from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Course, Folder, File
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .forms import UserForm,ProfileForm

ebook_file_types = ['pdf', 'doc', 'docx', 'epub', 'pdb', 'html', 'txt', 'mobi']


class IndexView(generic.ListView):
    template_name = "books/index.html"

    def get_queryset(self):
        return Course.objects.all()


def folders(request, course_id):
    all_folders = Folder.objects.all()
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'books/folders.html', {'all_folders': all_folders, 'course_id': course_id, 'course': course})


def files(request, course_id, folder_id):
    all_files = File.objects.all()
    course = get_object_or_404(Course, pk=course_id)
    folder = get_object_or_404(Folder, pk=folder_id)
    return render(request, 'books/files.html',
                  {'course_id': course_id, 'course': course, 'folder': folder,
                   'folder_id': folder_id, 'all_files': all_files})


class FileCreate(CreateView):
    model = File
    fields = ['course', 'file_type', 'file_name', 'file_path']


def download(request, course_id, folder_id):
    folder = get_object_or_404(Folder, pk=folder_id)
    course = get_object_or_404(Course, pk=course_id)
    all_files = File.objects.all()
    req_file = ''
    for file in all_files:
        if file.course == course and file.file_type == folder:
            req_file = req_file + file.filename()
            file_download = file.file_path
    response = HttpResponse(file_download.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % req_file
    return response


"""def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('books/index.html')
        else:
            return render(request, 'books/index.html')
    else:
        return render(request, 'books/index.html')"""

"""class UserFormView(View):
    form_class = UserForm
    template_name = 'books/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user.save()

            user = authenticate(name=name, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return  redirect('books:index')
        return render(request, self.template_name, {'form':form})"""


class UserFormView(View):
    form_class = UserForm
    form_class1 = ProfileForm
    template_name = 'books/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        form1 = self.form_class1(None)
        return render(request, self.template_name, {'form':form, 'form1':form1})

    def post(self,request):
        form = self.form_class(request.POST, instance=request.user)
        form1 = self.form_class1(request.POST, instance=request.user.profile)

        if form.is_valid() and form1.is_valid():

            user = form.save(commit=False)
            email = form.save()
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            user.save()
            form1.save()

            user = authenticate(name=name, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('books:index')
        return render(request, self.template_name, {'form': form, 'form1': form1})