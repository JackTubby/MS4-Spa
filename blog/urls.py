from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_blogs, name='blogs'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add_blog/', views.add_blog, name='add_blog'),
]
