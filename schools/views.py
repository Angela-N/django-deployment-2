from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, View
from schools.models import School, Student


# Create your views here.


class SchoolListView(ListView):  # default context name is <model_name>_list
    context_object_name = 'schools'
    model = School
    template_name = 'schools/schools.html'


class SchoolDetailView(DetailView):  # default context name is <model_name>
    model = School
    template_name = 'schools/school_details.html'
