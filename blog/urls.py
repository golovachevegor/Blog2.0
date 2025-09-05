from django.urls import path
from blog.views import *

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/create/', CommentCreateView.as_view(), name='comment_create_view'),
    path('post/tags/<slug:tag>/', PostByTagListView.as_view(), name='post_by_tags'),
    path('category/<slug:slug>/', PostFromCategory.as_view(), name='post_by_category'),
]
