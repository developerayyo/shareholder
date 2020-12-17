from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import User, ShareHolder

admin.site.register(User)

@admin.register(ShareHolder)
class ShareHolderAdmin(ImportExportModelAdmin):
    list_display = [field.name for field in ShareHolder._meta.get_fields()]
    # list_per_page = 1454
