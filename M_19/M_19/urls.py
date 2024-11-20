"""
URL configuration for M_19 project.

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
from django.contrib import admin
from django.urls import path
from task1.views import Task4, sign_up_by_django


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Task4.main_page),
    path('main/shop/', Task4.shop_page),
    path('main/basket/', Task4.basket_page),
    path('', sign_up_by_django),
    # path('django_sign_up', sign_up_by_html),
]
