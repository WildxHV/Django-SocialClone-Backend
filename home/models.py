from django.contrib.auth.models import AbstractUser, Permission, Group
from django.contrib.auth.base_user import BaseUserManager
from django.db import models

class UserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(
            email=email   
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):

        kwargs.setdefault("is_active", True)
        kwargs.setdefault("is_staff", True)
        kwargs.setdefault("is_superuser", True)

        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **kwargs)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, max_length=16)
    bio = models.CharField(max_length=164, null=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    groups = models.ManyToManyField(Group, related_name="user_groups", blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name="user_permissions", blank=True
    )
    
    

class Post(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=164)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class PostLike(models.Model):
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("post", "user"), )

class PostComment(models.Model):
    comment_text = models.CharField(max_length=264)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, on_delete=models.CASCADE)

class UserFollow(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="src_follow")
    follows = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="dest_follow")