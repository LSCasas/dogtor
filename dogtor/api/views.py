from django.shortcuts import render
from rest_framework import viewsets, generics

# Models
from vet.models import PetOwner, PetDate, Pet


# Serializers
from .serializers import OwnersSerializers, PetDateSerializers, PetSerializers, OwnersListSerializer, PetDateListSerializer, PetListSerializer



# # Create your views here.
# class OwnersViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo PetOwner."""

#     # Definir queryset y serializer_class dentro de la clase
#     queryset = PetOwner.objects.all()
#     serializer_class = OwnersSerializers
    


# class PetDateViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo PetDate."""

#     # Definir queryset y serializer_class dentro de la clase
#     queryset = PetDate.objects.all()
#     serializer_class = PetDateSerializers


# class PetViewSet(viewsets.ModelViewSet):
#     """ViewSet del modelo Pet."""

#     # Definir queryset y serializer_class dentro de la clase
#     queryset = Pet.objects.all()
#     serializer_class = PetSerializers

# OWNERS
class ListOwnersAPIView(generics.ListAPIView):
    """List Owners Api View"""
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer

class RetrievOwnersAPIView(generics.RetrieveAPIView):
    """Detail Pet Owner Api View."""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersListSerializer

class CreateOwnerAPIView(generics.CreateAPIView):
    """Create Pet Owner Api View"""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers

class UpdateOwnerAPIView(generics.UpdateAPIView):
    """Update Pet Owner Api View"""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers

class DeleteOwnerAPIView(generics.DestroyAPIView):
    """Delete Pet Owner Api View"""
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializers

# PET DATE
class ListPetDateAPIView(generics.ListAPIView):
    """List PetDate Api View"""
    queryset = PetDate.objects.all().order_by("created_at")
    serializer_class = PetDateListSerializer

class RetrievPetDateAPIView(generics.RetrieveAPIView):
    """Detail Pet Date Api View."""
    queryset = PetDate.objects.all()
    serializer_class = PetDateListSerializer

class CreatePetDateAPIView(generics.CreateAPIView):
    """Create Pet Date Api View"""
    queryset = PetDate.objects.all()
    serializer_class = PetDateSerializers

class UpdatePetDateAPIView(generics.UpdateAPIView):
    """Update Pet Date Api View"""
    queryset = PetDate.objects.all()
    serializer_class = PetDateSerializers

class DeletePetDateAPIView(generics.DestroyAPIView):
    """Delete Pet Date Api View"""
    queryset = PetDate.objects.all()
    serializer_class = PetDateSerializers

# PET
class ListPetAPIView(generics.ListAPIView):
    """List Pet Api View"""
    queryset = Pet.objects.all().order_by("created_at")
    serializer_class = PetListSerializer

class RetrievPetAPIView(generics.RetrieveAPIView):
    """Detail Pet Api View."""
    queryset = Pet.objects.all()
    serializer_class = PetListSerializer

class CreatePetAPIView(generics.CreateAPIView):
    """Create Pet Api View"""
    queryset = Pet.objects.all()
    serializer_class = PetSerializers

class UpdatePetAPIView(generics.UpdateAPIView):
    """Update Pet Api View"""
    queryset = Pet.objects.all()
    serializer_class = PetSerializers

class DeletePetAPIView(generics.DestroyAPIView):
    """Delete Pet Api View"""
    queryset = Pet.objects.all()
    serializer_class = PetSerializers