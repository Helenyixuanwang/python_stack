from django.db import models



# Create your models here.

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['name']) < 5:
            errors['name'] = "Name should be at least 5 characters"
        if len(postData['desc']) < 15:
            errors['desc'] = "Description should be at least 15 characters"
        return errors


class Description(models.Model): #one course has one description, one to one relationship, add 
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Course(models.Model):
    name = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True, blank=True)
    description = models.OneToOneField(Description, related_name="course",null=True,on_delete=models.CASCADE)#one to one with class Description
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = CourseManager()

class Comment(models.Model):# one course may havve many comments, so course vs. comments are one to many relationship
    comment = models.TextField()
    course = models.ForeignKey(Course, related_name = "comments" , on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
