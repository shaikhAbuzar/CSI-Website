from django.shortcuts import render
from .models import CarouselSlider
from Events.models import Event


# Created views here.
def home(request):
	carouselSlider = CarouselSlider.objects
	events = Event.objects.filter(status='upcoming').order_by('event_date', 'event_time')[: 3]
	if not events:
		events = None
	return render(request, r'home\home.html', {'sliders': carouselSlider, 'events': events})
