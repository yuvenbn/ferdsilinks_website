
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogPost, Category

        

class BlogQuerysetMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_categories'] = Category.objects.all()
        context['recent_posts'] = BlogPost.objects.order_by('-created_at')[:6]
        return context

class BlogPostListView(BlogQuerysetMixin, ListView):
    model = BlogPost
    template_name = 'blog/bp_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()

        # Check if a search query parameter is provided
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        # Check if a category filter is provided
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_links'] = ['blog']
        return context

class BlogPostDetailView(BlogQuerysetMixin, DetailView):
    model = BlogPost
    template_name = 'blog/bp_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_links'] = ['blog']
        context['post_categories'] = Category.objects.all()
        return context