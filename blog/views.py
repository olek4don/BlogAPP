from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
# from django.http import HttpResponse  # TODO: delete it

# posts = [
#     {
#         'author': 'AxelEf',
#         'title': 'Blog Post 1',
#         'content': 'Content 1',            # TODO: delete whole posts
#         'date_posted': 'December 23, 2022' # no longer need after modify 'posts' in context
#     },                                     # and since we have set SQL connection with database
#     {                                      # in Django shell
#         'author': 'Ada J',
#         'title': 'Blog Post 2',
#         'content': 'Content 2',
#         'date_posted': 'December 24, 2022'
#     }
# ]


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)
    # return HttpResponse('<h1>Blog Home</h1>')  # TODO: DELETE IT


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Blog'})
