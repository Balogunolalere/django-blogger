from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView,TemplateView
from .models import Blog
from django.urls import reverse_lazy
import requests
import json
from django.shortcuts import render
# Create your views here.
class HomeView(ListView):
	model = Blog
	template_name = 'index.html'

class CreateView(CreateView):
	model = Blog
	template_name = 'create.html'
	fields = ['title', 'author', 'body']
	success_url = reverse_lazy('index')


class PostView(DetailView):
	model = Blog
	template_name = 'post.html'



class DeleteView(DeleteView):
	model = Blog
	template_name = 'delete.html'
	success_url = reverse_lazy('index')


class UpdateView(UpdateView):
	model = Blog
	template_name = 'edit.html'
	fields = ['title', 'body']
	success_url = reverse_lazy('index')

class AboutView(TemplateView):
	model = Blog
	template_name = 'about.html'


class ContactView(TemplateView):
	model = Blog
	template_name = 'contact.html'

