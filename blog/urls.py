from django.urls import path

from .views import *

app_name = "blog"

urlpatterns = [
    # URL pattern for the blog post list (all)
    path('posts/', BlogPostListView.as_view(), name='bp-list'),

    # URL pattern for the blog post list with search filter
    path('posts/search/', BlogPostListView.as_view(), name='bp-list-search'),

    # URL pattern for the blog post list with category filter
    path('posts/category/<slug:category_slug>/', BlogPostListView.as_view(), name='bp-list-category'),

    # URL pattern for the blog post detail
    path('posts/<slug:slug>', BlogPostDetailView.as_view(), name='bp-detail'),
    
]
