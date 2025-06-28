from rest_framework import serializers
from .models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('__all__')
        read_only_fields = ('create_at',)
        