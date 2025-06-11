from django.shortcuts import render
from django.views.generic import ListView
from .models import PatientAccount


# Create your views here.
"""
Class-based views:

View        = generic view
ListView    = get a list of records
DetailView  = get a single(detail) record
CreateView  = create a new record
DeleteView  = remove a record
UpdateView  = modify an existing record
LoginView   = login
"""



# Create your views here.
def home_view(request):
    return render(request, 'pages/home.html')

def about_view(request):
    return render(request, 'pages/about.html')

def doctor_view(request):
    return render(request, 'pages/doctors.html')

def nurse_view(request):
    return render(request, 'pages/nurses.html')

def patient_view(request):
    return render(request, 'pages/patients.html')

def contact_view(request):
    return render(request, 'pages/contact.html')

class PatientAccountView(ListView):
    model = PatientAccount
    template_name = 'pages/patient_account.html'
    context_object_name = "all_accounts"


def patient_balance_view(request):
    return render(request, 'pages/patient_balance.html')

def referrals_view(request):
    return render(request, 'pages/referrals.html') 


