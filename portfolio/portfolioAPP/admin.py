from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import SendEmailForm
# Register your models here.
class EmailAdmin(ModelAdmin):
    list_display = ("name", "created_at", "email")
admin.site.register(SendEmailForm, EmailAdmin)
