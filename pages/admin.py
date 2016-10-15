from django.contrib import admin

from . import models


@admin.register(models.MailingListSignup)
class MailingListSignupAdmin(admin.ModelAdmin):
    pass