from django.urls import path, include
from .views import *
urlpatterns = [
    path('', simpleViewClass.as_view() ,name="home"),
    path('register/', simpleCreationForm.as_view() ,name="register"),
    path('dashboard/', dashboardViewClass.as_view() ,name="dashboard"),
    
]
