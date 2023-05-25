from rest_framework import serializers
from .models import *


class HomeSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSection
        fields = '__all__'


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['skill']


class SkillTypeSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = SkillType
        fields = ['type', 'skills']


class SkillSectionSerializer(serializers.ModelSerializer):
    skill_card_1 = SkillTypeSerializer(many=False, read_only=True)
    skill_card_2 = SkillTypeSerializer(many=False, read_only=True)
    skill_card_3 = SkillTypeSerializer(many=False, read_only=True)

    class Meta:
        model = SkillSection
        fields = '__all__'        


class ContactSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSection
        fields = ['contact_copy']
