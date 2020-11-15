from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from .models import Post
# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/index.html"
    paginate_by = 2


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"

