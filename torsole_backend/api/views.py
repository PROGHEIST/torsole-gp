from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GramPanchayatInfoSerializer, SlideShowSerializer, AboutVillageSerializer
from .models import GramPanchayatInfo, SlideShow, AboutVillage

class GramPanchayatInfoViewSet(viewsets.ModelViewSet):
    serializer_class = GramPanchayatInfoSerializer
    queryset = GramPanchayatInfo.objects.all()

class SlideShowViewSet(viewsets.ModelViewSet):
    serializer_class = SlideShowSerializer
    queryset = SlideShow.objects.all()

class AboutVillageViewset(viewsets.ModelViewSet):
    serializer_class = AboutVillageSerializer
    queryset = AboutVillage.objects.all()