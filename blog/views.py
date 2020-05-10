from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Post

def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)

class PostListView(ListView):
	models = Post
	template_name = 'blog/home.html' #<app>
	context_object_name = 'posts' 

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})