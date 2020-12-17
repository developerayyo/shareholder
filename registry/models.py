from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .validators import ASCIIUsernameValidator
from django_countries.fields import CountryField
from django.conf import settings


#Constants
MARITAL_STATUS = (
    ("Single", "Single"),
    ("Married", "Married"),
)

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

PAYMENT_MODE = (
    ("Cash", "Cash"),
    ("Cheque", "Cheque"),
    ("Transfer", "Transfer")
)

ENTITY = (
    ("Individual", "Individual"),
    ("Society", "Society"),
    ("Corporation", "Corporation"),
)

AREA_NAME = (
    ("Ogun", "Ogun"),
    ("Osun", "Osun"),
    ("Ondo", "Ondo"),
    ("Ekiti", "Ekiti"),
    ("Oyo", "Oyo"),
)
AREA_CODE = (
    ("OG", "OG"),
    ("OS", "OS"),
    ("ON", "ON"),
    ("EK", "EK"),
    ("OY", "OY"),
)

AREA_CLASS = (
    ("OGUN1 INDIVIDUAL", "OGUN1 INDIVIDUAL"),
    ("OGUN1 UNION", "OGUN1 UNION"),
    ("OGUN2 INDIVIDUAL", "OGUN2 INDIVIDUAL"),
    ("OGUN2 UNION", "OGUN2 UNION"),

    ("OSUN1 INDIVIDUAL", "OSUN1 INDIVIDUAL"),
    ("OSUN1 UNION", "OSUN1 UNION"),
    ("OSUN2 INDIVIDUAL", "OSUN2 INDIVIDUAL"),
    ("OSUN2 UNION", "OSUN2 UNION"),

    ("ONDO1 INDIVIDUAL", "OGUN1 INDIVIDUAL"),
    ("ONDO1 UNION", "OGUN1 UNION"),
    ("ONDO2 INDIVIDUAL", "ONDO2 INDIVIDUAL"),
    ("ONDO2 UNION", "ONDO2 UNION"),

    ("EKITI1 INDIVIDUAL", "EKITI1 INDIVIDUAL"),
    ("EKITI1 UNION", "EKITI1 UNION"),
    ("EKITI2 INDIVIDUAL", "EKITI2 INDIVIDUAL"),
    ("EKITI2 UNION", "EKITI2 UNION"),

    ("OYO1 INDIVIDUAL", "OYO1 INDIVIDUAL"),
    ("OYO1 UNION", "OYO1 UNION"),
    ("OYO2 INDIVIDUAL", "OYO2 INDIVIDUAL"),
    ("OYO2 UNION", "OYO2 UNION"),

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
    name = models.CharField(max_length=50,blank=True, null=True)
    share_holder_id = models.IntegerField(blank=True, null=True)
    social_security_number = models.IntegerField(blank=True, null=True)
    legacy_shareholder_id =  models.CharField(max_length=100)
    post_code = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    employee_number = models.IntegerField(blank=True, null=True)
    marital_status =  models.CharField(choices=MARITAL_STATUS, max_length=40, blank=True, null=True)
    sex = models.CharField(choices=GENDER, max_length=40, blank=True, null=True)
    country = models.CharField(blank=True, null=True, max_length=50)
    birth_date = models.CharField(max_length=50, blank=True, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    date_applied = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    bank = models.CharField(max_length=100, blank=True, null=True)
    bank_account_no = models.IntegerField(blank=True, null=True)
    email_address = models.EmailField(blank=True, null=True)
    payment_mode = models.CharField(choices=PAYMENT_MODE, max_length=50, blank=True, null=True)
    business_id = models.IntegerField(blank=True, null=True)
    share_qty = models.IntegerField(blank=True, null=True)
    unit_value = models.PositiveIntegerField(blank=True, null=True)
    share_value = models.PositiveIntegerField(blank=True, null=True)
    area_name = models.CharField(choices=AREA_NAME, max_length=50, blank=True, null=True)
    area_code = models.CharField(choices=AREA_CODE, max_length=50, blank=True, null=True)
    area_class = models.CharField(choices=AREA_CLASS, max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    entity = models.CharField(choices=ENTITY, max_length=50, blank=True, null=True)

    


