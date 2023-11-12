from django.db import models

from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    technology = models.CharField(max_length=70)
    image = models.FileField(upload_to="project_images/", blank=True)
