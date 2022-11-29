from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView
from django.views import View
from .models import Page, Post

class Home(View):
    def get(self, request, *args, **kwargs):
        items=Page.objects.all()
        return render(request, 'blog/index.html', {'items': items})

class PostList(ListView):
    queryset = Post.objects.filter().order_by('-created_date')
    template_name = 'blog/post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PageList(ListView):
    queryset = Page.objects.filter().order_by('-created_date')
    template_name = 'blog/page_list.html'

class PageDetail(DetailView):
    model = Page
    template_name = 'blog/page_detail.html'