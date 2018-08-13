from django.conf.urls import url
from events import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.event_home, name='events'),
    url(r'^planning_page/', views.planning_page, name='planning_page'),
    url(r'^form_page/', views.form_name_view, name='form_name'),
]
