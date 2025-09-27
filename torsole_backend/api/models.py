from django.db import models

class GramPanchayatInfo(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True)
    name = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class SlideShow(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='slideshow/', blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name