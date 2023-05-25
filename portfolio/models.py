from django.db import models


class HomeSection(models.Model):
    logo_text = models.CharField(max_length=6, verbose_name='Logo Initials')
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Home Section'    


class AboutSection(models.Model):
    about_bold_copy = models.TextField(null=True, blank=True, verbose_name='About Bold Copy')
    about_reg_copy = models.TextField(null=True, blank=True, verbose_name='About Regular Copy')

    def __str__(self) -> str:
        return self.about_bold_copy
    
    class Meta:
        verbose_name_plural = 'About Section'


class SkillSection(models.Model):
    skill_resume_url = models.CharField(max_length=1024, null=True, blank=True, verbose_name='Resume URL')
    skill_github_url = models.CharField(max_length=1024, null=True, blank=True, verbose_name='GitHub URL')
    skill_card_1 = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills1')
    skill_card_2 = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills2')
    skill_card_3 = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills3')

    class Meta:
        verbose_name_plural = 'Skill Section'


class SkillType(models.Model):
    """ Used in card titles in the Skill section """
    type = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Skill Type'

    def __str__(self) -> str:
        return self.type
    

class Skill(models.Model):
    """ Used in the cards in the Skill section """
    skill_type = models.ForeignKey('SkillType', on_delete=models.CASCADE, null=True, blank=True, related_name='skills')
    skill = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.skill
    

class ContactSection(models.Model):
    contact_copy = models.TextField(null=True, blank=True, verbose_name='Contact Copy')

    def __str__(self) -> str:
        return self.contact_copy
    
    class Meta:
        verbose_name_plural = 'Contact Section'
