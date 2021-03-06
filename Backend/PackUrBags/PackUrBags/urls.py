"""PackUrBags URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from authentication.api.views import HomeView
from django.conf import settings
from django.conf.urls import url
from django.views import static
from . import views
from guide.api.views import getToken
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    url(r'^assets/assets/(?P<path>.*)$', static.serve, {'document_root': settings.BASE_DIR + "/assets/assets"}),
    path('', views.index, name='home'),
    # path('',views.index,name='home'),
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.api.urls')),
    path('api/guide/', include('guide.api.urls')),
    path('api/', include('Tourism.api.urls')),
    path('api/', include('monuments.api.urls')),
    path('api/get-api-key', getToken.as_view(), name="get-api-key"),
    path('accounts/profile/', HomeView.as_view(), name="home"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
