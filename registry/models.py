from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ASCIIUsernameValidator


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
STATE = (
    ("OGUN", "OGUN"),
    ("OSUN", "OSUN"),
    ("ABUJA", "ABUJA"),
    ("LAGOS", "LAGOS"),
)
AREA = (
    ("OG1", "OG1"),
    ("OG2", "OG2"),
    ("OS1", "OS1"),
    ("OS2", "OS2"),
    ("ABJ1", "ABJ1"),
    ("ABJ2", "ABJ2"),
    ("LAG1", "LAG1"),
    ("LAG2", "LAG2")
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
    address = models.CharField(max_length=60, blank=True, null=True)
    SocialSecurityNumber = models.IntegerField(unique=True)
    LegacyShareholderID =  models.CharField(max_length=100)
    City = models.CharField(max_length=50)
    Area = models.CharField(max_length=50)
    AreaName = models.CharField(max_length=50)
    PostCode = models.IntegerField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    EmployeeNumber = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    MaritalStatus =  models.CharField(choices=MARITAL_STATUS, max_length=40)
    Sex = models.CharField(choices=GENDER, max_length=40)
    Domicile = models.CharField(max_length=50)
    BirthDate = models.DateField(blank=True, null=True)
    DateApplied = models.DateTimeField(blank=True, null=True)
    Phone = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    BankBankAccountNo = models.IntegerField()
    # EmailAddress = models.EmailField(blank=True, null=True)
    ShareQty = models.IntegerField()
    UnitValue = models.PositiveIntegerField()
    ShareValue = models.PositiveIntegerField()
    PaymentMode = models.CharField(choices=PAYMENT_MODE, max_length=50)
    State = models.CharField(choices=STATE, max_length=50)
    Area = models.CharField(choices=AREA, max_length=50)
    # PaymentMode
    # PrintChequeFlag
    # ReserveFlag   
    # WaiveFlag
    # Classification
    # Entity
    # ShareQty
    # ShareValue
    # EMailFlag
    # UnitValue
    # BusinessID
    def __str__(self):
        return self.name 


    


