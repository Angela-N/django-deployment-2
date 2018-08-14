from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from schools.models import School, Student
from django.urls import reverse_lazy


# Create your views here.


class SchoolListView(ListView):  # default context name is <model_name>_list
    context_object_name = 'schools'
    model = School
    template_name = 'schools/schools.html'


class SchoolDetailView(DetailView):  # default context name is <model_name>
    model = School
    template_name = 'schools/school_details.html'


class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'motto')
    model = School


class SchoolUpdateView(UpdateView):
    fields = ('principal',)
    model = School


class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy('schools:school_list')
