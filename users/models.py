from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
        
class Media(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_name = models.CharField(max_length=50)
    image_description = models.CharField(max_length=80)
    image_image = models.ImageField(upload_to='media', default='default.jpg')

    def __str__(self):
        return f'{self.user.username} Media'

