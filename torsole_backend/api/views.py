from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GramPanchayatInfoSerializer, SlideShowSerializer, AboutVillageSerializer, MissionSerializer, MissionObjectivesSerializer, ImportantLinksSerializer, GovernmentGRSerializer, DepartmentSerializer
from .models import GramPanchayatInfo, SlideShow, AboutVillage, Mission, MissionObjectives, ImportantLinks, GovernmentGR, Department

class GramPanchayatInfoViewSet(viewsets.ModelViewSet):
    serializer_class = GramPanchayatInfoSerializer
    queryset = GramPanchayatInfo.objects.all()

class SlideShowViewSet(viewsets.ModelViewSet):
    serializer_class = SlideShowSerializer
    queryset = SlideShow.objects.all()

class AboutVillageViewset(viewsets.ModelViewSet):
    serializer_class = AboutVillageSerializer
    queryset = AboutVillage.objects.all()

class MissionViewSet(viewsets.ModelViewSet):
    serializer_class = MissionSerializer
    queryset = Mission.objects.all()

class MissionObjectivesViewSet(viewsets.ModelViewSet):
    serializer_class = MissionObjectivesSerializer
    queryset = MissionObjectives.objects.all()

class ImportantLinksViewset(viewsets.ModelViewSet):
    serializer_class = ImportantLinksSerializer
    queryset = ImportantLinks.objects.all()

class GovernmentGRViewset(viewsets.ModelViewSet):
    serializer_class = GovernmentGRSerializer
    queryset = GovernmentGR.objects.all()

class DepartmentViewset(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()