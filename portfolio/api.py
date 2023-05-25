from rest_framework import permissions
from drf_multiple_model.views import ObjectMultipleModelAPIView

from .models import HomeSection, AboutSection, SkillSection, ContactSection
from .serializers import HomeSectionSerializer, AboutSectionSerializer, SkillSectionSerializer, ContactSectionSerializer


class MultipleModelPermissions(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        return True


class PortfolioAPIView(ObjectMultipleModelAPIView):
    permission_classes = (MultipleModelPermissions,)
    querylist = [
        {'queryset': HomeSection.objects.all(), 'serializer_class': HomeSectionSerializer, 'label': 'home'},
        {'queryset': AboutSection.objects.filter(), 'serializer_class': AboutSectionSerializer, 'label': 'about'},
        {'queryset': SkillSection.objects.all(), 'serializer_class': SkillSectionSerializer, 'label': 'skills'},
        {'queryset': ContactSection.objects.filter(), 'serializer_class': ContactSectionSerializer, 'label': 'contact'},
    ]
