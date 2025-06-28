from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer