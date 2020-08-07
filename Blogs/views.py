from django.shortcuts import render, get_object_or_404
from .models import Blogs


# Created views here.
def blogs_home(request):
	blogs = Blogs.objects.order_by('-date_of_article')
	if not blogs:
		blogs = None
	return render(request, r'Blogs\blogHome.html', {'blogs': blogs})


def full_blog(request, blog_id):
	blog = get_object_or_404(Blogs, pk=blog_id)
	return render(request, r'Blogs\FullBlog.html', {'blog': blog})
