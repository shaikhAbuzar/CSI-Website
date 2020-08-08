from django.shortcuts import render
from .models import Committie


# Created views here.
def members(request):
	faculty = Committie.objects.filter(Category='Faculty').order_by('Designation')
	president = Committie.objects.filter(Designation='President')[: 1]
	vice_president = Committie.objects.filter(Designation='Vice President')[: 1]
	secretary = Committie.objects.filter(Designation='Secretary')
	joint_secretary = Committie.objects.filter(Designation='Joint Secretary')
	sponsorship = Committie.objects.filter(Designation='Sponsorship Head')
	joint_sponsorship = Committie.objects.filter(Designation='Joint Sponsorship Head')
	pr = Committie.objects.filter(Designation='PR Head')
	joint_pr = Committie.objects.filter(Designation='Joint PR Head')
	technical = Committie.objects.filter(Designation='Technical Head')
	joint_technical = Committie.objects.filter(Designation='Joint Technical Head')
	creative = Committie.objects.filter(Designation='Creative Head')
	joint_creative = Committie.objects.filter(Designation='Joint Creative Head')
	organizing = Committie.objects.filter(Designation='Organizing Head')
	joint_organizing = Committie.objects.filter(Designation='Joint Organizing Head')
	magazine = Committie.objects.filter(Designation='Magazine Head')
	joint_magazine = Committie.objects.filter(Designation='Joint Magazine Head')
	treasurer = Committie.objects.filter(Designation='Treasurer')
	joint_treasurer = Committie.objects.filter(Designation='Joint Treasurer')
	dictionary = {
		'faculties': faculty,
		'president': president,
		'vice_president': vice_president,
		'secretary': secretary,
		'joint_secretary': joint_secretary,
		'sponsorship': sponsorship,
		'joint_sponsorship': joint_sponsorship,
		'pr': pr,
		'joint_pr': joint_pr,
		'technical': technical,
		'joint_technical': joint_technical,
		'creative': creative,
		'joint_creative': joint_creative,
		'organizing': organizing,
		'joint_organizing': joint_organizing,
		'magazine': magazine,
		'joint_magazine': joint_magazine,
		'treasurer': treasurer,
		'joint_treasurer': joint_treasurer,
	}
	return render(request, r'committie\members.html', dictionary)
