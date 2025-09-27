from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from django.http import HttpResponse
from .forms import NoteForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.

def index(request):
    notes = Note.objects.all()
    return render(request, 'notes/base.html', {'notes':notes})

@login_required
def create(request):
    if request.method == "POST": #this is what happens if the submit/create button is pressed
        form = NoteForm(request.POST) #the form is assigned to all the information from the form that the user submitted
        if form.is_valid():

            t = form.cleaned_data["title"]
            c = form.cleaned_data["content"]
            n = Note(title=t, content=c)
            n.user = request.user
            n.save()
            

            return redirect('view') # just use the name no need for the path
            
    else:
        form = NoteForm() #the alternative to POST is GET and "GET" would mean that is the first time the page is being opened
    
    return render(request, 'notes/create.html', {'form':form})

@login_required
def  view(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/view.html', {'notes':notes})
    
def delete(request, id):
    note = get_object_or_404(Note, id=id) #find the note based on id
    note.delete()
    return redirect('view')

def edit(request, id):
    note = get_object_or_404(Note, id=id)
   
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid:
            form.save()
            return redirect('view')
        
    else:
        form = NoteForm(instance=note)
    
    return render(request, 'notes/edit.html', {'form':form})


        
