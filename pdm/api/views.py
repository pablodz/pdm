# views.py
from rest_framework import viewsets


# from api.serializers import HeroSerializer
from .serializers import medichypertableSerializer
from .serializers import lastmedichypertableSerializer
# from api.models import Hero
from .models import medic_hypertable

class medichypertableViewSet(viewsets.ModelViewSet):
     queryset = medic_hypertable.objects.all().order_by('time')
     serializer_class = medichypertableSerializer

class lastmedichypertableViewSet(viewsets.ModelViewSet):
     queryset = medic_hypertable.objects.all().order_by('-time')[:1]
     serializer_class = lastmedichypertableSerializer

# class HeroViewSet(viewsets.ModelViewSet):
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer