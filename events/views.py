from django.shortcuts import render
from django.http import HttpResponse
from events.forms import FormName
from events.models import Topic, WebPage, AccessRecords


def index(request):
    return HttpResponse("<em>Hello World</em>")


# Create your views here.
def event_home(request):
    # grab all pages from AccessRecords db by date
    web_pages = AccessRecords.objects.order_by('date')  # list
    date_dict = {'access_records': web_pages}
    return render(request, 'events/events.html', context=date_dict)


def planning_page(request):
    my_list = ['apples', 'pears', 'bananas', 'mangoes', 'strawberries']
    #  return render(request, PlanningPage.html, context = myList)
    my_dict = {'var': 'HEY, I AM THE TEMPLATE TAG', 'var2': my_list}
    return render(request, 'PlanningPage.html', context=my_dict)


def chat_bot(request):
    weather_list = ['sunny', 'windy', 'cloudy', 'snowy', 'rainy']
    my_dict = {'var3': weather_list}
    return render(request, 'PlanningPage.html', context=my_dict)


def form_name_view(request):
    form = FormName()
    # Check to see if we get a post back.
    if request.method == 'POST':
        # In which case we pass in that request
        form = FormName(request.POST)
        # check to see if form is valid
        if form.is_valid():
            print(" Form validation is successful")
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])
    return render(request, 'events/form_name.html', {'form': form})
