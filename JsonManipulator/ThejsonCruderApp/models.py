from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator
from django.utils import timezone

class Account(models.Model):
    agent_name = models.CharField(max_length=255)
    corporate_name = models.CharField(max_length=255)
    corporate_type_id = models.CharField(max_length=50)
    pcc_code = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    office_number = models.CharField(max_length=20)
    customer_category_id = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    time_zone_key = models.CharField(max_length=50)
    corporate_address = models.TextField()
    pos_code = models.CharField(max_length=10)
    corporate_status = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])

class Contact(models.Model):
    confirm_code = models.CharField(max_length=255, unique=True)
    account_id = models.CharField(max_length=255, default='')
    user_name = models.CharField(max_length=255)
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_id = models.EmailField(validators=[EmailValidator()])
    user_address = models.TextField()
    country_code = models.CharField(max_length=2)
    city_id = models.CharField(max_length=255)
    user_zip_code = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    phone_number = models.CharField(max_length=20)
    approved_status = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])





class Relation(models.Model):
    reference_id = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255 , default='')
    corporate_id = models.CharField(max_length=255, default='')
    is_direct = models.BooleanField()
    active_status = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])




class JsonData(models.Model):
    json_file = models.FileField(upload_to='json_files/',default='No values')


