import jwt
from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, phone, email, password):
        if not username:
            raise ValueError("Provide a Username!")
        if not phone:
            raise ValueError("Provide a Phone Number!")
        if not email:
            raise ValueError("Provide an Email!")
        if not password:
            raise ValueError("Enter Password!")
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username = username,
            phone = phone,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, username, phone, email, password):
        if password is None:
            raise ValueError("Superuser must have a Password!")
        user = self.create_user(first_name, last_name, username, phone, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user