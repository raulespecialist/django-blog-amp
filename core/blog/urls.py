from django.urls import path, include
from .views import Home, PageList, PageDetail, PostList, PostDetail
urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pages/', PageList.as_view(), name='page_list'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('<slug:slug>/', PageDetail.as_view(), name='page_detail'),
    path('blog/<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]