from django.shortcuts import render


# Created views here.
def events_home(request):
	return render(request, r'Events/eventsHome.html')
