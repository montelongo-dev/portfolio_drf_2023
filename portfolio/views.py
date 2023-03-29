from rest_framework import generics
from rest_framework.response import Response

from .models import *
from .serializers import PortfolioSerializer


class PortfolioViewSet(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = PortfolioSerializer(queryset, many=True)
        return Response(serializer.data)
