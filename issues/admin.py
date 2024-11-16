from django.contrib import admin
from .models import Issue

class IssueAdmin(admin.ModelAdmin):
      list_display = ['title', 'priority', 'status', 'created_at']
      list_filter = ['priority', 'status']
      search_fields = ['title', 'description']
      
