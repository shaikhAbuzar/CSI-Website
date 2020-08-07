from django.shortcuts import render


# Created views here.
def blogs_home(request):
	return render(request, r'Blogs\blogHome.html')
