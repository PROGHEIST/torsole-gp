from rest_framework import serializers
from .models import GramPanchayatInfo, SlideShow, AboutVillage

class GramPanchayatInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GramPanchayatInfo
        fields = '__all__'

class SlideShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlideShow
        fields = '__all__'
    
class AboutVillageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutVillage
        fields = '__all__'
        