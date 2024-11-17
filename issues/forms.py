from django import forms
from django.contrib.auth import get_user_model  
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'priority', 'status', 'assignee']
        widgets = {
            'summary': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter a brief summary of the issue'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Provide a detailed description of the issue',
                'rows': 5
            }),
            'priority': forms.Select(attrs={
                'class': 'form-control'
            }),
            'status': forms.Select(attrs={
                'class': 'form-control'
            }),
            'assignee': forms.Select(attrs={
                'class': 'form-control'
            })
        }

    
    assignee = forms.ModelChoiceField(queryset=get_user_model().objects.all(), required=False, empty_label="Select Assignee")
