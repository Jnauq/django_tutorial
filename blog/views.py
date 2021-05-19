from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'    # Assign which template to use in ListView  default: <app>/<model>_<list>.html
    context_object_name = 'posts'       # Change var name of object to loop over
    ordering = ['-date_posted']         # Adding - reverses ordering by attribute
    paginate_by = 5                     # Num posts per page


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'      # Assign which template to use in ListView
    context_object_name = 'posts'               # Change var name of object to loop over
    paginate_by = 5                             # Num posts per page

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post                        # Default template: blog/post_detail.html


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post                        # Default template: blog/post_form.html
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user    # Take current logged in user and set as form instance's author
        return super().form_valid(form)             # Call parent form_valid() with modified form instance


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post                        # Default template: blog/post_form.html
    fields = ['title', 'content']
    success_url = '/'

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
    return render(request, 'blog/about.html', { 'title': 'About' })
