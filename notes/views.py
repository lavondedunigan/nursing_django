from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, DeleteView
from .models import Note
from django.urls import reverse_lazy



#Create your views here.
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
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView

# Create your views here.
class NoteList(ListView):
    model = Note
    template_name = 'notes/list.html'
    
    
    
class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'content', 'image']
    template_name = 'notes/details.html'
    success_url = reverse_lazy('notes:list')
    

    
    
    
    
    
    
    