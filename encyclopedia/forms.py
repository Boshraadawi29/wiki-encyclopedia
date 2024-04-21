from django import forms
from . import util
from django.core.exceptions import ValidationError
class MyForm(forms.Form): 
    Title = forms.CharField(max_length = 20, required = True, widget=forms.TextInput(attrs= {'class': "form-control", 'size': '20', 'placeholder': 'Enter the title of the new entry'}))
    Content = forms.CharField(min_length=20, required = True, widget=forms.Textarea(attrs= {'class': "form-control",'size': '20', 'placeholder': 'Please ensure that the information you provide is accurate and relevant.'}))
    
    
    
    def clean_Title(self): 
    	title = self.cleaned_data['Title']
    	if any(title.lower() == entry.lower() for entry in util.list_entries()):
            raise ValidationError('This entry already exists!')
    	return title

