from rest_framework import serializers
from .models import GramPanchayatInfo, SlideShow, AboutVillage, Mission, MissionObjectives, ImportantLinks, GovernmentGR, Department

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

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class MissionObjectivesSerializer(serializers.ModelSerializer):
    missions = MissionSerializer(many=True, read_only=True)

    class Meta:
        model = MissionObjectives
        fields = '__all__'
        
class ImportantLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantLinks
        fields = '__all__'

class GovernmentGRSerializer(serializers.ModelSerializer):
    class Meta:
        model = GovernmentGR
        fields = '__all__'
    
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'