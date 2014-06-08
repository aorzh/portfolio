from django.contrib import admin
from pages.models import Page, PageAdmin

admin.site.register(Page, PageAdmin)
