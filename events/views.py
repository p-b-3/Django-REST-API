from django.shortcuts import render
from rest_framework import generics, renderers
from .models import Conference, Person, Company
from .serializers import ConferenceSerializer, PersonSerializer

# Create your views here.
class ConferenceList(generics.ListCreateAPIView):
    #renderer_classes = renderers.JSONRenderer
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer

class ConferenceDetail(generics.RetrieveUpdateDestroyAPIView):
    #renderer_classes = renderers.JSONRenderer
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer


class PeopleList(generics.ListCreateAPIView):
    #renderer_classes = renderers.JSONRenderer
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
