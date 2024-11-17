from django.urls import path
from .views import (
    IssueListView, IssueDetailView,
    IssueCreateView, IssueUpdateView, IssueDeleteView, update_issue_status
)

app_name = "issues"

urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('new/', IssueCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='delete'),
    path('update-status/', update_issue_status, name='update_status')
]