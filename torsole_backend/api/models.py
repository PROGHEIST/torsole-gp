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

class AboutVillage(models.Model):
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[0:100]

class Mission(models.Model):
    mission = models.TextField(blank=True)

    def __str__(self):
        return self.mission

class MissionObjectives(models.Model):
    heading = models.CharField(max_length=300, blank=True)
    missions = models.ManyToManyField(Mission, blank=True, related_name='objectives')

    def __str__(self):
        return self.heading

class ImportantLinks(models.Model):
    title = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="important-links/", blank=True)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Department(models.Model):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
    
class GovernmentGR(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="grs")
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="gr_files/")
    category = models.CharField(max_length=100, blank=True, null=True)
    date_issued = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.department.name})"

class GramPanchayatDocuments(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="gp_documents/")
    category = models.CharField(max_length=100, blank=True, null=True)
    date_issued = models.DateField()
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PhotoGallery(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="photo_gallery/")
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

