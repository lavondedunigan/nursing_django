from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, DeleteView
from .models import Note, NoteComment
from django.urls import reverse_lazy
from .forms import NoteForm



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

# Create your views here.
class NoteList(ListView):
    model = Note
    template_name = 'notes/list.html'
       
class NoteCreate(CreateView):
    model = Note
    fields = ['title', 'content', 'image']
    template_name = 'notes/details.html'
    success_url = reverse_lazy('notes:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Note"
        return context
        
  
  
class NoteDetail(DetailView):
    model = Note
    template_name = "notes/details.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # load all comments related to the note
        note = self.object
        comments = NoteComment.objects.filter(note=note).prefetch_related('author')
        context['comments'] = comments
        return context
 
 
    
class NoteUpdate(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = "notes/create.html"
    success_url = reverse_lazy('notes:list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update Note"
        return context
    

class NoteDelete(DeleteView):
    model = Note
    template_name = "notes/delete.html"
    success_url = reverse_lazy('note_list')

       
    

    
    
    
    
    
    
