from typing import BinaryIO
from django.db import models
from datetime import datetime,timedelta
import re # the regex model

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # birth date must be in the past
        today = datetime.now().strftime("%Y-%m-%d")
        form_data = postData['birth']
        print(datetime.now())
        print(today)
        print(form_data)
        if form_data > today:
            errors['birthdate'] = "birthday must be in the past"
       
       # add keys and values to errors dictionary for each invalid field
        FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z ]+$') # fist name check, should be letters
        if not  FIRST_NAME_REGEX.match(postData['f_name']):             
            errors['first_name_format'] = "Invalid name format"
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


        #if (postData['birth']) < strip(): # birth date set in past
            #errors['birth'] = "birth date must be in the past"


        users_with_email = User.objects.filter(email = postData['email']) 
        if len(users_with_email) >=1:
            errors['users_duplicate'] = "Email address taken already, choose another"
        
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.TextField()
    birthday = models.DateTimeField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    
