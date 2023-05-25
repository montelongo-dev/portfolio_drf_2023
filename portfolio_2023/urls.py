from django.contrib import admin
from django.urls import path

from portfolio import api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/portfolio', api.PortfolioAPIView.as_view(), name='portfolio'),
]
