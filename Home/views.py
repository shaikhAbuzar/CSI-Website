from django.shortcuts import render
from django.core.mail import send_mail
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
	return render(request, r'home/home.html', {'sliders': carouselSlider, 'events': events, 'blogs': blogs, 'mail': 'unsent'})


def sent_mail(request):
	carouselSlider = CarouselSlider.objects
	events = Event.objects.filter(status='upcoming').order_by('event_date', 'event_time')[: 3]
	blogs = Blogs.objects.order_by('-date_of_article')[: 5]
	if not events:
		events = None
	if not Blogs:
		blogs = None

	if request.method == 'POST':
		name = request.POST['name']
		sender_email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		body = f'You have received a message from {name}\nThe message is:\n{message}'
		send_mail(
			subject,
			body,
			sender_email,
			['kecif59098@intsv.net', 'shaikhzartan@gmail.com'],
			fail_silently=False
		)
		dictionary = {'sliders': carouselSlider, 'events': events, 'blogs': blogs, 'mail': 'sent'}
		return render(request, r'home/home.html', dictionary)
	else:
		return render(request, r'home/home.html', {'sliders': carouselSlider, 'events': events, 'blogs': blogs, 'mail': 'unsent'})
