from django.shortcuts import render
from users.models import UserModel
from users.forms import UserModelForm, ContactForm
from django.views.generic import FormView


# Create your views here.
def users(request):
    user_list = UserModel.objects.order_by('first_name')
    return render(request, 'users/users.html', {'users': user_list})


def register_users(request):
    form = UserModelForm
    if request.method == 'POST':
        form = UserModelForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print('Error, Form is Invalid')

    return render(request, 'users/users_register.html', {'form': form})


def contact_us_view(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('Good Form!')
            print(f"first name: {form.cleaned_data['first_name']}")
            print(f"last name: {form.cleaned_data['last_name']}")
            return users(request)
        else:
            print('ERROR')

    return render(request, 'users/users_register.html', {'form': form})


# Class Based View
class ContactUsView(FormView):
    template_name = 'users/users_register.html'
    form_class = ContactForm
    success_url = '/users'

    def form_valid(self, form):
        print('Good Form!')
        print(f"first name: {form.cleaned_data['first_name']}")
        print(f"last name: {form.cleaned_data['last_name']}")
        return super().form_valid(form)
