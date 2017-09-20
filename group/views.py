from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Group,GroupMember

# Create your views here.

class CreateGroup(LoginRequiredMixin, generic.CreateView):
    model = Group
    fields = ['name','description']

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group