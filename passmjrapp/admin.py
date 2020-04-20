from django.contrib import admin
from .models import *
from .forms import *
from import_export.admin import ImportExportModelAdmin

@admin.register(PasswordAccount)
class ViewAdmin(ImportExportModelAdmin):
    pass


# class CreatePassAdmin(admin.ModelAdmin):
#     list_display = ['title',
#                   'username',
#                   'password',
#                   'url',
#                   'additional_notes']
#     form = CreatePassForm
#     list_filter = ['username']
#     search_fields = ['title']