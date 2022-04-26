from ast import Pass
from django.contrib import admin
from .models import PasswordAccount, PasswordGroup
from import_export.admin import ImportExportModelAdmin


admin.site.register(PasswordGroup)


@admin.register(PasswordAccount)
class ViewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'group', 'username', 'password', 'url', 'additional_notes']
    list_filter = ['user']
    search_fields = ['title'],
    list_editable = ['group']





