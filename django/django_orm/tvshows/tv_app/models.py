from django.db import models

# Create your models here

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters"
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters"
        if len(postData['desc']) < 10:
            errors['desc'] = "Description should be at least 10 characters"    
        return errors

class Show(models.Model):
    title=models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects=ShowManager()  #newly added to link the ShowManager