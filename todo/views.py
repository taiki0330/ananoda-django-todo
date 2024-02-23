from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import TodoModel
from django.urls import reverse_lazy

# Create your views here.
class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel

class TodoDetail(DetailView):
    model = TodoModel
    template_name = "detail.html"

class TodoCreate(CreateView):
    model = TodoModel
    template_name = "create.html"
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')

class TodoDelete(DeleteView):
    model = TodoModel
    template_name = "delete.html"
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    model = TodoModel
    template_name = "update.html"
    success_url = reverse_lazy('list')
    fields = ('title', 'memo', 'priority', 'duedate')



