from django.shortcuts import render
from django.views.generic import View

from blog.models import Post

# Create your views here.
class BlogListView(View):
    def get(self, request, **kwargs):
        posts = Post.objects.all()
        
        return render(request,
        'blog/list.html',
        { 'posts': posts })