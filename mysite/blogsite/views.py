from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comment, Post, Category
from .forms import CommentForm, PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# ListView allows us to list a query set into the database or display multiple blog posts at once
# DetailView only pulls a single item from the database or in this case one blog post per page
# CreateView lets us create blog posts
# UpdateView lets us edit blog posts
# DeleteView deletes the post
# See more here: https://docs.djangoproject.com/en/4.1/ref/class-based-views/generic-display/
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
        
# cats is the name of the variable containing the string used in the urls.py file and this must match.
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category__name__iexact=cats.title().replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        blog_stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = blog_stuff.total_likes()

        liked = False
        if blog_stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

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
