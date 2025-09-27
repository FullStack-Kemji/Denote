from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
           
            'title':forms.TextInput(attrs={'class':'form-control mb-3', 'placeholder':'Enter Title'}),  # how to edit a crispy form
            'content':forms.Textarea(attrs={'class':'form-control mb-3', 'rows': 3 }),
            #text area allows me to mainpulate the amount of space for typing in a crispy form

        }