from django.urls import path
from .views import list_pet_owners, Test, OwnersList

urlpatterns = [
    path("owners/", OwnersList.as_view()),
    path("test/", Test.as_view()),

]