from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone

from blog.models import Post

# Create your views here.
class BlogListView(View):
    def get(self, request, **kwargs):
        now = timezone.now()
        posts = Post.objects.filter(
            published_date__lte=now
        ).order_by('-published_date')
        
        return render(request,
        'blog/list.html',
        { 'posts': posts })


class BlogDetailView(View):
    def get(self, request, **kwargs):
        return render(
            request,
            'blog/detail.html',
            {'post':post}
        )