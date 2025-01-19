from django.urls import path
from .views import OwnersList, OwnerDetail, PetList, PetDetail, Test, OwnersCreate, OwnersUpdate, PetCreate, PetUpdate
urlpatterns = [
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnerDetail.as_view(), name="owner_detail"),
    path("owners/add/", OwnersCreate.as_view(), name="owners_create"),
    path("pets/add/", PetCreate.as_view(), name="pets_create"),
    path("pets/<int:pk>/edit/", PetUpdate.as_view(), name="pets_create"),
    path("owners/<int:pk>/edit/", OwnersUpdate.as_view(), name="owners_create"),
    path("pets/", PetList.as_view(), name="pet_list"),
    path("pets/<int:pk>/", PetDetail.as_view(), name="pet_detail"),
    path("test/", Test.as_view(), name="test"),
]
