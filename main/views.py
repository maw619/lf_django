from urllib import request
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'main/home.html')

@login_required
def projects(request):
    title = "L.F Jennings | PROJECTS"
    projects = AppLfprojects.objects.raw(
        "Select * From app_lfprojects order by pr_desc")
    return render(request, 'main/projects.html', {'data':projects, 'title':title})

@login_required
def reports(request):
    title = "L.F Jennings | REPORTS"
    reports = AppLfreportes.objects.raw(
        "Select * From app_lfreportes inner join app_lfprojects on rep_fk_pr_key = pr_key inner join app_lfemployees on rep_fk_emp_key = emp_key")
    return render(request, 'main/reports.html', {'data': reports, 'title':title})

@login_required
def employees(request):
    title = "L.F Jennings | EMPLOYEES"
    employees = AppLfemployees.objects.raw(
        " Select * From app_lfemployees inner join app_lfcargos on emp_fk_ch_key = ch_key")
    return render(request, 'main/employees.html', {'data':employees, 'title':title})

@login_required
def charges(request):
    title = "L.F Jennings | CHARGES"
    return render(request, 'main/charges.html', {'title':title})

@login_required
def photos(request):
    title = "L.F Jennings | PHOTOS"
    photos = AppLfphotos.objects.all()
    return render(request, 'main/photos.html', {'data':photos, 'title':title})

@login_required
def certifications(request):
    title = "L.F Jennings | CERTIFICATIONS"
    return render(request, 'main/certifications.html', {'title':title})


def open(request):
    return render(request, 'main/open.html')