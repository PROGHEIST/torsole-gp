from django.shortcuts import render
from rest_framework import viewsets
from .serializers import GramPanchayatInfoSerializer, SlideShowSerializer
from .models import GramPanchayatInfo, SlideShow

class GramPanchayatInfoViewSet(viewsets.ModelViewSet):
    serializer_class = GramPanchayatInfoSerializer
    queryset = GramPanchayatInfo.objects.all()

class SlideShowViewSet(viewsets.ModelViewSet):
    serializer_class = SlideShowSerializer
    queryset = SlideShow.objects.all()