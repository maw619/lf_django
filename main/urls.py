from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('reports', views.reports,  name='reports'),
    path('employees', views.employees, name='employees'),
    path('charges', views.charges,  name='charges'),
    path('photos', views.photos,  name='photos'),
    path('certifications', views.certifications,  name='certifications'),
    path('open', views.open,  name='open'),
]