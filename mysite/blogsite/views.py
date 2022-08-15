from unicodedata import category
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# ListView allows us to list a query set into the database or display multiple blog posts at once
# DetailView only pulls a single item from the database or in this case one blog post per page
# CreateView lets us create blog posts
# UpdateView lets us edit blog posts
# DeleteView deletes the post
# See more here: https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/

class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']
# cats is the name of the variable containing the string used in the urls.py file and this must match.
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats)
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    # can only use either form_class or fields at once so, choose wisely!
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
