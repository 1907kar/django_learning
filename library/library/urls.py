"""
URL configuration for library project.

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
from django.urls import path, include

# Below import is done manually inorder to redirect from home page to respective url
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),  
    # The url needs to be provided as url path
    path('', RedirectView.as_view(url="catalog/")),
    # This is contrib urls responibile for handling all the login/passwordreset..etc
    # All the linked urls are available at the django source code level
    path('accounts/', include('django.contrib.auth.urls')),

]
