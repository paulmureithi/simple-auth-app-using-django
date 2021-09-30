from django.contrib.auth.models import User
import uuid
from uuid import uuid4
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    profile_pic = models.ImageField(blank=True, default='profiles/default.jpg', upload_to='profiles/')
    country = models.CharField(blank=True, max_length=200, default='Kenya')
    short_bio = models.TextField(blank=True, default='No bio..')
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.first_name )   