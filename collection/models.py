from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Timestamp(models.Model):
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True)

    class Meta: 
        abstract = True

class Thing(Timestamp): 
    name = models.CharField(max_length = 255) 
    description = models.TextField() 
    slug = models.SlugField(unique = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
        blank=True, null = True)

    # new helper method
    def get_absolute_url(self):
        return "/things/%s/" % self.slug


class Social(models.Model):
    SOCIAL_TYPES = (
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
        ('pinterest', 'Pinterest'),
        ('instagram', 'Instagram'),
    )
    network = models.CharField(max_length=255, choices=SOCIAL_TYPES)
    username = models.CharField(max_length=255)
    thing = models.ForeignKey(Thing, on_delete=models.CASCADE, related_name="social_accounts")
    
    # where we're overriding the admin name
    class Meta:
        verbose_name_plural = "Social media links"