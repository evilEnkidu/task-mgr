from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
import json
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Issue, Status
from .forms import IssueForm
from accounts.models import CustomUser, Role, Team
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class IssueListView(LoginRequiredMixin, ListView):
    model = Issue
    template_name = 'issues/list.html'
    context_object_name = 'issues'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        team = user.team
        role = Role.objects.get(name="product owner")
        team_po = (
            CustomUser.objects
            .filter(team=team)
            .filter(role=role)
        )
        to_do = Status.objects.get(name="to do")
        context["to_do_list"] = (
            Issue.objects
            .filter(status=to_do)
            .filter(reporter=self.request.user)
            .order_by("created_on").reverse()
        )    
        in_progress = Status.objects.get(name="in progress")
        context["in_progress_list"] = (
            Issue.objects
            .filter(status=in_progress)
            .filter(reporter=self.request.user)
            .order_by("created_on").reverse()
        )
        done = Status.objects.get(name="done")
        context["done_list"] = (
            Issue.objects
            .filter(status=done)
            .filter(reporter=self.request.user)
            .order_by("created_on").reverse()
        )
        return context

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import ensure_csrf_cookie
import json

@require_POST
@ensure_csrf_cookie
def update_issue_status(request):
    try:
        data = json.loads(request.body)
        issue_id = data.get('issue_id')
        new_status = data.get('status')
        
        print(f"Updating issue {issue_id} to status: {new_status}")  # Debug logging
        
        try:
            issue = Issue.objects.get(id=issue_id)
            status = Status.objects.get(name=new_status)
            
            # Verify user has permission to update this issue
            if issue.reporter != request.user:
                return JsonResponse({
                    'error': 'Permission denied'
                }, status=403)
            
            issue.status = status
            issue.save()
            
            return JsonResponse({
                'status': 'success',
                'message': f'Updated issue {issue_id} to status {new_status}'
            })
            
        except Issue.DoesNotExist:
            return JsonResponse({
                'error': f'Issue {issue_id} not found'
            }, status=404)
        except Status.DoesNotExist:
            return JsonResponse({
                'error': f'Invalid status: {new_status}'
            }, status=400)
            
    except Exception as e:
        print(f"Error updating status: {str(e)}")  # Debug logging
        return JsonResponse({
            'error': str(e)
        }, status=500)

class IssueDetailView(LoginRequiredMixin, DetailView):
    model = Issue
    template_name = 'issues/detail.html'

class IssueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Issue
    template_name = 'issues/new.html'
    form_class = IssueForm
    success_url = reverse_lazy('issues:list')
    

    def test_func(self):
        role = Role.objects.get(name="product owner")
        return self.request.user.role == role

    def form_valid(self, form):
        form.instance.reporter = self.request.user
        return super().form_valid(form)

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView ):
    model = Issue
    template_name = 'issues/edit.html'
    fields = ['summary', 'description', 'assignee', 'priority', 'status']
    success_url = reverse_lazy('issues:list')

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.reporter

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    template_name = 'issues/delete.html'
    success_url = reverse_lazy('issues:list')

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.reporter