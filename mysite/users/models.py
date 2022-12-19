from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
# from django.contrib.auth.models import User
from PIL import Image
from main.models import Product

#
# class User(models.Model):
#     city = models.TextField(max_length=50)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    orders = models.ManyToManyField(Product, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'


def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


def post_save_profile_create(sender, instance, created, *args, **kwargs):
        if created:
            Profile.objects.get_or_create(user=instance)


post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)

