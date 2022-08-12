from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
# ListView allows us to list a query set into the database or display multiple blog posts at once
# DetailView only pulls a single item from the database or in this case one blog post per page
# See more here: https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/

# Create your views here.
# def index(request):
#     return render(request, 'index.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = '__all__'