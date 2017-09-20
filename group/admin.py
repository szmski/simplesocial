from django.contrib import admin
from . import models

# Register your models here.

class GroupMemberInline(admin.TabluarInline):
    model = models.GroupMember

admin.site.register(models.Group)