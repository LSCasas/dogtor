from django.contrib import admin
from . import models
# Register your models here.




#Panel de administracion para la app de 'blog'
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel administracion"""

    site_header = "Blog Site Admin Area"

#Instanciar nuestra clase
blog_admin_site = BlogAdminArea(name="BlogAdmin")


#registramos modelo 'Post' en nuestro admin area
blog_admin_site.register(models.Post)


#Registrarlo en el admin area general de admin
admin.site.register(models.Post)