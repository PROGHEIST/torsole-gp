from rest_framework import serializers
from .models import GramPanchayatInfo, SlideShow

class GramPanchayatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GramPanchayatInfo
        fields = '__all__'

class SlideShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideShow
        fields = '__all__'