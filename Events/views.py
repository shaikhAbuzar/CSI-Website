from django.shortcuts import render, get_object_or_404
from .models import Event


# Created views here.
def events_home(request):
	upcoming_events = Event.objects.filter(status='upcoming').order_by('event_date', 'event_time')[: 3]
	if not upcoming_events:
		upcoming_events = None
	past_events = Event.objects.filter(status='completed').order_by('-event_date', '-event_time')[: 3]
	return render(request, r'Events/eventsHome.html', {'upcoming_events': upcoming_events, 'past_events': past_events})


def event_details(request, event_id):
	event = get_object_or_404(Event, pk=event_id)
	return render(request, r'Events/eventDetails.html', {'event': event})


# TODO More Events Page
def all_events(request, event_type):
	if "past" in event_type.lower():
		events = Event.objects.filter(status='completed').order_by('-event_date', '-event_time')
	else:
		events = Event.objects.filter(status='upcoming').order_by('event_date', 'event_time')
	return render(request, r'Events/moreEvents.html', {'eventTitle': event_type, 'events': events})
