from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ASCIIUsernameValidator
from django_countries.fields import CountryField


#Constants
MARITAL_STATUS = (
    ("SINGLE", "SINGLE"),
    ("MARRIED", "MARRIED")
)

GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE")
)

PAYMENT_MODE = (
    ("CASH", "CASH"),
    ("CHEQUE", "CHEQUE"),
    ("TRANSFER", "TRANSFER")
)

ENTITY = (
    ("INDIVIDUAL", "INDIVIDUAL"),
    ("SOCIETY", "SOCIETY"),
    ("CORPORATION", "CORPORATION")
)

STATE = (
    ("OGUN", "OGUN"),
    ("OSUN", "OSUN"),
    ("ABUJA", "ABUJA"),
    ("LAGOS", "LAGOS"),
)
AREA = (
    ("OG", "OG"),
    ("OS", "OS"),
    ("AB", "AB"),
    ("LA", "LA")
)


# Create your models here.
class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    picture = models.ImageField(upload_to="pictures/", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    username_validator = ASCIIUsernameValidator()

    def get_picture(self):
        no_picture = settings.STATIC_URL + 'assets/img/img_avatar.png'
        try:
            return self.picture.url
        except:
            return no_picture

    def get_full_name(self):
        full_name = self.username
        if self.first_name and self.last_name:
            full_name = self.first_name + " " + self.last_name
        return full_name

class ShareHolder(models.Model):
    name = models.CharField(max_length=50)
    ShareHolderId = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    SocialSecurityNumber = models.IntegerField(unique=True)
    LegacyShareholderID =  models.CharField(max_length=100)
    PostCode = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    EmployeeNumber = models.IntegerField(blank=True, null=True)
    MaritalStatus =  models.CharField(choices=MARITAL_STATUS, max_length=40)
    Sex = models.CharField(choices=GENDER, max_length=40)
    country = CountryField(blank=True, null=True)
    BirthDate = models.DateField(blank=True, null=True)
    DateApplied = models.DateTimeField(blank=True, null=True)
    Phone = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    BankBankAccountNo = models.IntegerField()
    EmailAddress = models.EmailField(blank=True, null=True)
    PaymentMode = models.CharField(choices=PAYMENT_MODE, max_length=50, blank=True, null=True)
    BusinessID = models.IntegerField(blank=True, null=True)
    ShareQty = models.IntegerField(blank=True, null=True)
    UnitValue = models.PositiveIntegerField(blank=True, null=True)
    ShareValue = models.PositiveIntegerField(blank=True, null=True)
    AreaName = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

# class Area(models.Model):
#     name = models.CharField()


    


