from django.urls import path, include
from rest_framework import routers

#views
# from .views import  ListOwnersAPIView, RetrievOwnersAPIView
from .views import ListOwnersAPIView, RetrievOwnersAPIView, CreateOwnerAPIView, UpdateOwnerAPIView, DeleteOwnerAPIView
from .views import ListPetDateAPIView, RetrievPetDateAPIView, CreatePetDateAPIView, UpdatePetDateAPIView, DeletePetDateAPIView
from .views import ListPetAPIView, RetrievPetAPIView, CreatePetAPIView, UpdatePetAPIView, DeletePetAPIView


# #Router
# router = routers.DefaultRouter()
# router.register(r"owners", OwnersViewSet)
# router.register(r"petDate", PetDateViewSet)
# router.register(r"pets", PetViewSet)

urlpatterns = [
    # OWNERS
    path("owners/", ListOwnersAPIView.as_view(), name="owners_list"),
    path("owners/<int:pk>/", RetrievOwnersAPIView.as_view(), name="owners_detail"),
    path("owners/create/", CreateOwnerAPIView.as_view(), name="owners_create"),
    path("owners/<int:pk>/update/", UpdateOwnerAPIView.as_view(), name="owners_update"),
    path("owners/<int:pk>/delete/", DeleteOwnerAPIView.as_view(), name="owners_delete"),

    # PET DATE
    path("petdate/", ListPetDateAPIView.as_view(), name="petdate_list"),
    path("petdate/<int:pk>/", RetrievPetDateAPIView.as_view(), name="petdate_detail"),
    path("petdate/create/", CreatePetDateAPIView.as_view(), name="petdate_create"),
    path("petdate/<int:pk>/update/", UpdatePetDateAPIView.as_view(), name="petdate_update"),
    path("petdate/<int:pk>/delete/", DeletePetDateAPIView.as_view(), name="petdate_delete"),

    # PET
    path("pets/", ListPetAPIView.as_view(), name="pets_list"),
    path("pets/<int:pk>/", RetrievPetAPIView.as_view(), name="pets_detail"),
    path("pets/create/", CreatePetAPIView.as_view(), name="pets_create"),
    path("pets/<int:pk>/update/", UpdatePetAPIView.as_view(), name="pets_update"),
    path("pets/<int:pk>/delete/", DeletePetAPIView.as_view(), name="pets_delete")
]
