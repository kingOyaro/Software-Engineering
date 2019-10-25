"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.contrib import admin
from django.conf.urls import url

from product import views
from profiles import views as profiles_views
from contact import views as contact_views
from checkout import views as checkout_views
from product import views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', profiles_views.home, name='home'),
    path('about/', profiles_views.about, name='about'),
    path('profile/', profiles_views.userProfile, name='profile'),
    path('checkout/', checkout_views.checkout, name='checkout'),
    path('contact/', contact_views.contact, name='contact'),
    path('product/', include('product.urls'), name='product'),
    path('cart/', include('cart.urls'), name='cart'),
    path('accounts/', include('allauth.urls')),

]

urlpatterns += staticfiles_urlpatterns()
