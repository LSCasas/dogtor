from django.contrib import admin

# Register your models here.
#Panel de administracion para la app de 'blog'
class BlogAdminArea(admin.AdminSite):
    """Blog admin panel administracion"""

    site_header = "Blog Site Admin Area"

#Instanciar nuestra clase
blog_admin_site = BlogAdminArea(name="BlogAdmin")