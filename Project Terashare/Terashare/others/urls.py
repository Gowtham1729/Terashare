from django.conf.urls import url
from . import views
app_name = 'others'

urlpatterns = [
    # books/
    url(r'^$', views.index, name='index'),
    ]