from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Drawing)
admin.site.register(models.Compartments)
admin.site.register(models.Aircraft)