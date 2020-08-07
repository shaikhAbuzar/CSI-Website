from django.shortcuts import render
from .models import CarouselSlider
from Events.models import Event
from Blogs.models import Blogs


# Created views here.
def home(request):
	carouselSlider = CarouselSlider.objects
	events = Event.objects.filter(status='upcoming').order_by('event_date', 'event_time')[: 3]
	blogs = Blogs.objects.order_by('-date_of_article')[: 5]
	if not events:
		events = None
	if not Blogs:
		blogs = None
	return render(request, r'home\home.html', {'sliders': carouselSlider, 'events': events, 'blogs': blogs})
