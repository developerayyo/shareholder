from django.contrib import admin

# Register your models here.
from .models import User, ShareHolder

admin.site.register(User)

admin.site.register(ShareHolder)
