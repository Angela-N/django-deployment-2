from django.conf.urls import url
from schools import views

app_name = 'schools'

urlpatterns = [
    url(r'^$', views.SchoolListView.as_view(), name='school_list'),
    url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school_details'),
    url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
]
