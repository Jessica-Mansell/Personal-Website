from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post
from .forms import PostForm, EditForm

# ListView allows us to list a query set into the database or display multiple blog posts at once
# DetailView only pulls a single item from the database or in this case one blog post per page
# See more here: https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class UpdatePostView(UpdateView):
    model = Post
    # can only use either form_class or fields at once so, choose wisely!
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']
