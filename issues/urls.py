from django.urls import path
from .views import (
    IssueListView, IssueDetailView,
    IssueCreateView, IssueUpdateView, IssueDeleteView
)

urlpatterns = [
    path('', IssueListView.as_view(), name='list'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('new/', IssueCreateView.as_view(), name='new'),
    path('<int:pk>/edit/', IssueUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', IssueDeleteView.as_view(), name='delete'),
]