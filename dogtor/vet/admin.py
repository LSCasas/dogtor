from django.contrib import admin
from . import models
# Register your models here.

#Panel de administracion para la app de 'blog'

class VetAdminArea(admin.AdminSite):
    """Vet admin panel administracion"""
    site_header = "Vet Site Admin Area"

#Instanciar nuestra clase

vet_admin_site = VetAdminArea(name="VetAdmin")


#registramos modelo 'Post' en nuestro admin area
vet_admin_site.register(models.PetOwner)
vet_admin_site.register(models.Pet)
vet_admin_site.register(models.PetDate)


#Registrarlo en el admin area general de admin
admin.site.register(models.PetOwner)
admin.site.register(models.Pet)
admin.site.register(models.PetDate)