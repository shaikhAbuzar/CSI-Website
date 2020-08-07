from django.shortcuts import render
from .models import CarouselSlider


# Created views here.
def home(request):
	carouselSlider = CarouselSlider.objects
	return render(request, r'home\home.html', {'sliders': carouselSlider})
