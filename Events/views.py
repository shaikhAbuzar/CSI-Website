from django.shortcuts import render
from .models import Event


# Created views here.
def events_home(request):
	upcoming_events = Event.objects.filter(status='upcoming').order_by('event_date', 'event_time')[: 3]
	if not upcoming_events:
		upcoming_events = None
	past_events = Event.objects.filter(status='completed').order_by('-event_date', '-event_time')[: 3]
	return render(request, r'Events/eventsHome.html', {'upcoming_events': upcoming_events, 'past_events': past_events})


def upcoming_event_details(request):
	return render(request, r'Events\upcomingEvent.html')


def past_event_details(request):
	return render(request, r'Events\pastEvent.html')