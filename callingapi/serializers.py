from rest_framework import serializers
from .models import CallingList

class CallingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallingList
        fields = '__all__'

