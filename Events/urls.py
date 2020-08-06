from django.urls import path
from . import views

urlpatterns = [
	path('', views.events_home, name='eventsHome'),
	path('<int:event_id>/', views.event_details, name='event_details'),
	path('<str:event_type>/', views.all_events, name='all_events')
]
