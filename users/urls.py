from django.conf.urls import url
from users import views

app_name = 'users'

urlpatterns = [
    url(r'^$', views.users, name='users'),
    url(r'^register/', views.register_users, name='register'),
    url(r'^contact_us/', views.ContactUsView.as_view(), name='contact_us'),
]
