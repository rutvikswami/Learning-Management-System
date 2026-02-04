from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,password=None,**ef):
        
        if not email:
            raise ValueError("email is required")
        
        email = self.normalize_email(email)

        user = self.model(email=email,**ef)

        user.set_password(password)

        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password=None,**ef):

        ef.setdefault('is_staff',True)
        ef.setdefault('is_superuser',True)
        ef.setdefault('is_active',True)

        if ef.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True")
        if ef.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True")
        
        return self.create_user(email,password,**ef)
    
