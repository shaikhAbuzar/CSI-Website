from django.urls import path
from . import views

urlpatterns = [
	path('', views.blogs_home, name='blogs_home'),
	path('<int:blog_id>/', views.full_blog, name='full_blog'),
]