from django.conf.urls import url
from schools import views

app_name = 'schools'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='school_list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school_details'),
]
