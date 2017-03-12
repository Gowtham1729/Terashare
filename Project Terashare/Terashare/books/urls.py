from django.conf.urls import url
from . import views

app_name = "books"

urlpatterns = [
    # books/
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # books/2
    url(r'^(?P<course_id>[0-9]+)/$', views.folders, name='folders'),
    # books/2/1
    url(r'^(?P<course_id>[0-9]+)/(?P<folder_id>[0-9]+)/$', views.files, name='files'),
    url(r'^add-file/$', views.FileCreate.as_view(), name='add-file'),
    url(r'^(?P<course_id>[0-9]+)/(?P<folder_id>[0-9]+)/download/$', views.download, name='download')
]
