from django.contrib import admin
from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """Post Admin model for admin"""
    fields = ["name"]  # Solo permite agregar el campo 'name'


# Panel de administración para la app de 'blog'
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel administración"""

    site_header = "Blog Site Admin Area"


# Instanciar nuestra clase
blog_admin_site = BlogAdminArea(name="BlogAdmin")

# Registramos modelo 'Post' en nuestro admin area personalizado
blog_admin_site.register(models.Post, PostAdmin)

# Registrarlo en el admin area general de admin
admin.site.register(models.Post, PostAdmin)
