from django.db import models
from django.db.models.deletion import CASCADE

import re # the regex model


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class BookManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['title']) < 1:
            errors['title'] = "added book must have a title"
        if len(postData['desc']) ==0 :
            errors['desc'] = "You must say something about book description"
            
        return errors


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        FIRST_NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')
        if not  FIRST_NAME_REGEX.match(postData['f_name']):             
            errors['first_name_format'] = "Invalid name"
        # add keys and values to errors dictionary for each invalid field
        if len(postData['f_name']) < 2:
            errors['f_name'] = "First name should be at least 2 characters"
        if len(postData['l_name']) < 2:
            errors['l_name'] = "Last name should be at least 2 characters"
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
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #books_loaded = a list of books uploaded by certain user
    #liked_books = a list of books favored by a certain user

    objects = UserManager()
    

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="books_loaded", on_delete=CASCADE)
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BookManager()