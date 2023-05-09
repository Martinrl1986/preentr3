from django.shortcuts import render
from .models import HomePage, AboutPage, ResumePage, ServicePage


def home_view(request):
    # Obtener los datos de la sección Home desde la base de datos
    home_data = HomePage.objects.first()  # Obtener el primer objeto de la tabla HomePage

    return render(request, 'home.html', {'home_data': home_data})

def about_view(request):
    # Obtener los datos de la sección About desde la base de datos
    about_data = AboutPage.objects.first()  # Obtener el primer objeto de la tabla AboutPage

    return render(request, 'about.html', {'about_data': about_data})

def resume_view(request):
    # Obtener los datos de la sección Resume desde la base de datos
    resume_data = ResumePage.objects.first()  # Obtener el primer objeto de la tabla ResumePage

    return render(request, 'resume.html', {'resume_data': resume_data})

def service_view(request):
    # Obtener los datos de la sección Service desde la base de datos
    service_data = ServicePage.objects.first()  # Obtener el primer objeto de la tabla ServicePage

    return render(request, 'service.html', {'service_data': service_data})
