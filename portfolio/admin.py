from django.contrib import admin
from .models import *


admin.site.register(Portfolio)
admin.site.register(SkillType)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'skill_type', )
