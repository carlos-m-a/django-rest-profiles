from rest_framework import serializers
from .models import Profile

class MySerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["user"]