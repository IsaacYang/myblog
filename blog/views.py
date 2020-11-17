from django.shortcuts import render,get_object_or_404,reverse,redirect
from django.views.generic import ListView, DetailView 
from .models import Post
from .forms import CommentForm
# Create your views here.


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/index.html"
    # paginate_by = 2


# class PostDetailView(DetailView):
#     model = Post
#     template_name = "blog/post_detail.html"

def post_detail(request,slug):
    template = "blog/post_detail.html" 
    post = get_object_or_404(Post,slug=slug)
    comments = post.comments.filter(active=True)
    if request.method=='POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            new_form=comment_form.save(commit=False)
            new_form.post=post
            new_form.save()
            return redirect(reverse("blog:post_detail",kwargs={'slug':slug}))
    else:
        comment_form = CommentForm()
    return render(request,template,{"post":post,"comments":comments,"comment_form":comment_form})