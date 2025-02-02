from django.shortcuts import render
from rest_framework import viewsets

# Models
from vet.models import PetOwner
from vet.models import PetDate
from vet.models import Pet

# Serializers
from .serializers import OwnersSerializers
from .serializers import PetDateSerializers
from .serializers import PetSerializers


# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetOwner."""

    # Definir queryset y serializer_class dentro de la clase
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers


class PetDateViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo PetDate."""

    # Definir queryset y serializer_class dentro de la clase
    queryset = PetDate.objects.all()
    serializer_class = PetDateSerializers


class PetViewSet(viewsets.ModelViewSet):
    """ViewSet del modelo Pet."""

    # Definir queryset y serializer_class dentro de la clase
    queryset = Pet.objects.all()
    serializer_class = PetSerializers
