from django import forms
from .models import Issue

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'priority', 'status']
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
            })
        }