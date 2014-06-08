from django.contrib import admin
from examples.models import Project, ProjectAdmin

admin.site.register(Project, ProjectAdmin)
