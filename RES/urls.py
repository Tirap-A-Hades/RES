"""
URL configuration for RES project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import SimpleRouter

import real_estate_card.views
import users.views
from real_estate_card.views import EstateView
from users.views import RegisterView

router = SimpleRouter()

router.register('api/estates', EstateView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', real_estate_card.views.index, name='index'),
    path('reestr/', real_estate_card.views.reestr, name='reestr'),
    path('estates/update', real_estate_card.views.object_update, name='object_edit'),
    path('estates/create', real_estate_card.views.objectcard, name='object_create'),
    path('users/reg/', RegisterView.as_view(), name='register'),
    path('support/', users.views.support, name='support'),
    path('estate/1/', real_estate_card.views.estate_card, name='estate'),
    path('users/', include('users.urls'), name='estate'),
]

urlpatterns += router.urls

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
