from django.db import models

# Create your models here.

import re # the regex model

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['f_name']) < 2:
            errors['f_name'] = "First name should be at least 2 characters"
        if len(postData['l_name']) < 3:
            errors['l_name'] = "Last name should be at least 3 characters"
        if len(postData['email']) < 6:
            errors['email'] = "Email should be at least 6 characters" 
        if len(postData['pw']) < 8:
            errors['password'] = "Password should be at least 9 characters"
        if postData['pw'] != postData['pw_conf']:
            errors['match'] = "User or password do not match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['regex'] = "Invalid email format!"

        users_with_email = User.objects.filter(email = postData['email']) 
        if len(users_with_email) >=1:
            errors['users_duplicate'] = "Email address taken already, choose another"
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


# Create your models here.
# User vs. Message: one to many
class Message(models.Model):
    message = models.TextField()
    message_img = models.ImageField(null=True, blank=True,upload_to="images/%y")
    user = models.ForeignKey(User,related_name="user_messages", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#User vs. Commnet: one to many
# Message vs. Comment: one to many
class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name="message_comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
