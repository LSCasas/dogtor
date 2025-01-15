from django.urls import path
from .views import OwnersList, OwnerDetail, PetList, PetDetail, Test

urlpatterns = [
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnerDetail.as_view(), name="owner_detail"),
    path("pets/", PetList.as_view(), name="pet_list"),
    path("pets/<int:pk>/", PetDetail.as_view(), name="pet_detail"),
    path("test/", Test.as_view(), name="test"),
]
