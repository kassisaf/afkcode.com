from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('blog/page=<int:page>', views.blog_index, name='blog_index_paged'),
    path('blog/page=<int:page>&posts=<int:posts_per_page>', views.blog_index, name='blog_index_paged'),
    path('blog/<int:pk>-<slug:slug>', views.blog_detail, name='blog_detail'),
    path('blog/<int:year>/<int:month>/<int:pk>-<slug:slug>', views.blog_detail_with_date, name='blog_detail_with_date'),
    path('category/<category>/', views.blog_category, name='blog_category'),
]
