from django.db import models

class HomePage(models.Model):
    # Campos para la sección Home
    class Meta:
        app_label = 'Miapp'
        
    title = models.CharField(max_length=1000)
    content = models.TextField()

class AboutPage(models.Model):
    # Campos para la sección About
    class Meta:
        app_label = 'Miapp'
        
    title = models.CharField(max_length=100)
    content = models.TextField()

class ResumePage(models.Model):
    # Campos para la sección Resume
    class Meta:
        app_label = 'Miapp'
        
    title = models.CharField(max_length=100)
    content = models.TextField()

class ServicePage(models.Model):
    # Campos para la sección Service
    class Meta:
        app_label = 'Miapp'
        
    title = models.CharField(max_length=100)
    content = models.TextField()

    