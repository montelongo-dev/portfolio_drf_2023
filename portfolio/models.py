from django.db import models


class Portfolio(models.Model):
    logo_text = models.CharField(max_length=6, verbose_name='Logo Initials')
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)

    about_bold_copy = models.TextField(null=True, blank=True, verbose_name='About Bold Copy')
    about_reg_copy = models.TextField(null=True, blank=True, verbose_name='About Regular Copy')

    skill_resume_url = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Resume URL')
    skill_card_1 = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills1')
    skill_card_2 = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills2')
    skill_card_3 = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills3')

    contact_copy = models.TextField(null=True, blank=True, verbose_name='Contact Copy')

    def __str__(self):
        return self.name


class SkillType(models.Model):
    type = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.type
    

class Skill(models.Model):
    skill_type = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills')
    skill = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.skill