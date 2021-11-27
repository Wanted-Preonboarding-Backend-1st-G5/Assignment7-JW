"""cardoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls                    import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers         import SimpleRouter

from tires.views                    import UserTireViewSet

app_name = 'tires'

router = SimpleRouter(trailing_slash=False)

router.register('tires', UserTireViewSet, basename='tires')
urlpatterns = router.urls

urlpatterns += [
    path('users', include('users.urls')),
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]