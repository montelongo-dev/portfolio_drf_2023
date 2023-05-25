from django.contrib import admin
from .models import *


admin.site.register(HomeSection)
admin.site.register(AboutSection)
admin.site.register(SkillSection)
admin.site.register(ContactSection)

admin.site.register(SkillType)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill', 'skill_type', )
