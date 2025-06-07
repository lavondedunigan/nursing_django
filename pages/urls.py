from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="root"),   
    path('home/', views.home_view, name="home"),
    path('about/', views.about_view, name="about"),
    path('doctors/', views.doctor_view, name="doctors"),
    path('nurses/', views.nurse_view, name="nurses"),
    path('patients/', views.patient_view, name="patients"),
    path('contact/', views.contact_view, name="contact"),
    
    path('patient_account/', views.patient_account_view, name="patient-account"),
    path('patient_balance/', views.patient_balance_view, name="patient-balance"),
    path('referrals/', views.referrals_view, name="referrals"),
   
]















