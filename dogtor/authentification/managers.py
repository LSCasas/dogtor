from django.contrib.auth.models import BaseUserManager

class ModUserManager(BaseUserManager):
    """Mod User Custom Manager"""

    def create_user(self, email, user_name, first_name, password, **other_fields):
        """Overiding create_user func for ModUserManager"""
        if not email:
            raise ValueError("You must provide an email...")
        email = self.normalize_email(email)
        user = self.model(email=email, user_name= user_name, first_name=first_name, **other_fields)

        user.set_password(password)

        user.save()

        return user
    
    def create_superuser(self, email, user_name, first_name, password, **other_fields):
        """Overiding create_superuser func for ModUserManager"""
        other_fields.setdefault("is_staff", True)
        other_fields.setdefault("is_activate", True)
        other_fields.setdefault("is_superuser", True)

        return self.create_user(email, user_name, first_name, password, **other_fields)



