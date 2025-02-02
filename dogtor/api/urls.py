from django.urls import path, include
from rest_framework import routers

#views
from .views import OwnersViewSet, PetDateViewSet, PetViewSet


#Router
router = routers.DefaultRouter()
router.register(r"owners", OwnersViewSet)
router.register(r"petDate", PetDateViewSet)
router.register(r"pets", PetViewSet)

urlpatterns = [
    path("", include(router.urls))
]

