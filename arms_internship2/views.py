from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View


def home(request):
    # return HttpResponse("<h1>HOME page</h1>Hello World")
    my_dict = {'var': 'HEY, I AM THE TEMPLATE TAG'}
    return render(request, 'index.html', context=my_dict)


# basic CBV
# class HomeView(View):
#     def get(self, request):
#         # return HttpResponse("CBV's Welcome!")
#         return render(request, 'index.html')


# class HomeView(TemplateView):
#     template_name = 'index.html'

# inject context
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(*kwargs)
        context['key'] = 'My context data'
        return context
