from rest_framework import serializers

# Models
from vet.models import PetOwner, PetDate, Pet



class OwnersSerializers(serializers.HyperlinkedModelSerializer):
    """Pet owners serializer."""
    class Meta:  
        model = PetOwner
        fields = [
            "first_name",
            "last_name",
            "address",
            "email",
            "phone",
            "created_at"
        ]


class PetDateSerializers(serializers.HyperlinkedModelSerializer):
    """PetDate serializer."""

    class Meta:
        model = PetDate
        fields = [
            "type",  # 'type' está relacionado con 'PetDate'
            "created_at",
            "pet"  # Agregado el campo de la relación 'pet'
        ]


class PetSerializers(serializers.HyperlinkedModelSerializer):
    """Pet serializer."""
    owner = serializers.PrimaryKeyRelatedField(queryset=PetOwner.objects.all(), many=False)

    class Meta:  # Cambié 'meta' por 'Meta'
        model = Pet
        fields = [
            "name",
            "type",
            "created_at",
            "owner"
        ]



# OWNERS
class OwnersListSerializer(serializers.ModelSerializer):
    """Serializer to list all Post Owners"""
    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name"]

class OwnersDetailSerializer(serializers.ModelSerializer):
    """Serializer for the detail of a Pet Owner."""
    class Meta:
        model = PetOwner
        fields = "__all__"


# OWNERS
class PetDateListSerializer(serializers.ModelSerializer):
    """Serializer to list all Post Pet Date"""
    class Meta:
        model = PetDate
        fields = "__all__"


# PET
class PetListSerializer(serializers.ModelSerializer):
    """Serializer to list all Post Pet """
    class Meta:
        model = Pet
        fields = "__all__"