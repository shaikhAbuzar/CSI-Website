from django.shortcuts import render
from .models import Committie

# Create your views here.

def members(request): 
    faculty = Committie.objects.filter(Category='Faculty')
    president = Committie.objects.filter(Designation='President')
    vice_president= Committie.objects.filter(Designation='Vice President')
    secretary= Committie.objects.filter(Designation='Secretary')
    joint_secretary= Committie.objects.filter(Designation='Joint Secretary')
    sponsorship= Committie.objects.filter(Designation='Sponsorship Head')
    joint_sponsorship= Committie.objects.filter(Designation='Joint Sponsorship')
    pr= Committie.objects.filter(Designation='PR Head')
    joint_pr= Committie.objects.filter(Designation='Joint PR')
    technical= Committie.objects.filter(Designation='Technical Head')
    joint_technical= Committie.objects.filter(Designation='Joint Technical')
    creative= Committie.objects.filter(Designation='Creative Head')
    joint_creative= Committie.objects.filter(Designation='Joint Creative')
    organizing= Committie.objects.filter(Designation='Organizing Head')
    joint_organizing= Committie.objects.filter(Designation='Joint Organizing')
    magazine= Committie.objects.filter(Designation='Magazine Head')
    joint_magazine= Committie.objects.filter(Designation='Joint Magazine')
    treasurer= Committie.objects.filter(Designation='Treasurer')
    membership= Committie.objects.filter(Designation='Membership')
    # print('committie object printed:',comm)
    return render(request,r'committie\members.html',{'faculties':faculty,
                                                    'president':president,
                                                    'vice_president':vice_president,
                                                    'secretary':secretary,
                                                    'joint_sceretary':joint_secretary,
                                                    'sponsorship':sponsorship,
                                                    'joint_sponsorship':joint_sponsorship,
                                                    'pr':pr,
                                                    'joint_pr':joint_pr,
                                                    'technical':technical,
                                                    'joint_technical':joint_technical,
                                                    'creative':creative,
                                                    'joint_creative':joint_creative,
                                                    'organizing':organizing,
                                                    'joint_organizing':joint_organizing,
                                                    'magazine':magazine,
                                                    'joint_magazine':joint_magazine,
                                                    'treasurer':treasurer,
                                                    'membership':membership})
