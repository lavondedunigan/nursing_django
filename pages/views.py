from django.shortcuts import render


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


