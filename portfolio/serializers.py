from rest_framework import serializers

from .models import *


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill']


class SkillTypeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = SkillType
        fields = ['type', 'skills']


class PortfolioSerializer(serializers.ModelSerializer):
    skill_card_1 = SkillTypeSerializer(many=False, read_only=True)
    skill_card_2 = SkillTypeSerializer(many=False, read_only=True)
    skill_card_3 = SkillTypeSerializer(many=False, read_only=True)

    class Meta:
        model = Portfolio
        fields = ['id', 'logo_text', 'name', 'title', 'about_bold_copy', 'about_reg_copy', 
                  'skill_resume_url', 'skill_card_1', 'skill_card_2', 'skill_card_3', 'contact_copy']

    