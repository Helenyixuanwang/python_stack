# from django.core.exceptions import ValidationError
# from django.db import models

# # our validator
# def validateLengthGreaterThanTwo(value):
#     if len(value) < 3:
#         raise ValidationError(
#             '{} must be longer than: 2'.format(value)
#         )

# # Create your models here.
# class User(models.Model):
#     first_name = models.CharField(max_length=255,validators = [validateLengthGreaterThanTwo])
#     last_name =  models.CharField(max_length=255,validators = [validateLengthGreaterThanTwo])
#     email = models.CharField(max_length=255)
#     password = models.CharField(max_length=255)
    
    
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
