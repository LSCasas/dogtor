from django.contrib.auth.models import BaseUserManager

class ModUserManager(BaseUserManager):
    """Mod User Custom Manager"""
    #1. create_user
    # ale -> 123456
    def create_user(self, email, user_name, first_name, password, **other_fields):
        """Overiding create_user func for ModUserManager"""
        # Agregar validacioens
        if not email:
            raise ValueError("You must provide an email...")
        #Ponemos en minusculas
        email = self.normalize_email(email)
        #Nos hizo el usuario en la variable 'user'
        user = self.model(email=email, user_name= user_name, first_name=first_name, **other_fields)
        #Seteamos password
        user.set_password(password)
        #Guardamos en base de datos
        user.save()
        return user
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """Overiding create_superuser func for ModUserManager"""
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_active", True)
        other_fields.setdefault("is_superuser", True)

        return self.create_user(email, user_name, first_name, password, **other_fields)



