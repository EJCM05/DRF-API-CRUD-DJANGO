from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth.forms import * # ¡Este es el formulario de login de Django!
from django.contrib.auth import login, logout # Funciones para iniciar/cerrar sesión
from django.urls import reverse_lazy # Para redirigir a una URL por su nombre

class simpleViewClass(FormView):
    # Esto renderiza un template html
    template_name = 'views/index.html' 
    form_class = AuthenticationForm #usamos el formulario de django
    success_url = reverse_lazy('dashboard') # Redirige a la URL con nombre 'index' al iniciar sesión correctamente
    
    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)    
    
    def form_invalid(self, form):
        return super().invalid(form)
    
class simpleCreationForm(CreateView):
    template_name = 'views/createUser.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    
    
class dashboardViewClass(TemplateView):
    # Esto renderiza un template html
    template_name = 'views/dashboard.html'