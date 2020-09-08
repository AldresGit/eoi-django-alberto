
from django.contrib import admin
from django.urls import path

from blog.views import BlogListView

urlpatterns = [
    # path('blog/', include='blog.urls')
    path('', BlogListView.as_view(), name='blog.list'),
    # path('/blog', BlogDetailView.as_view(), name='blog.detail'),
    path('admin/', admin.site.urls),
]
