from django.contrib import admin
from .models import PasswordAccount
from .forms import CreateUserForm, CreatePassForm, UpdatePassForm
from import_export.admin import ImportExportModelAdmin

@admin.register(PasswordAccount)
class ViewAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'username', 'password', 'url', 'additional_notes']
    form = CreatePassForm
    list_filter = ['user']
    search_fields = ['title']

# class CreatePassAdmin(admin.ModelAdmin):
#     list_display = ['title',
#                   'username',
#                   'password',
#                   'url',
#                   'additional_notes']
#     form = CreatePassForm
#     list_filter = ['user']
#     search_fields = ['title']

# @admin.register(PasswordAccount)
# class ViewAdmin(ImportExportModelAdmin, CreatePassAdmin):
#     pass
# # admin.site.register(PasswordAccount, CreatePassAdmin)



