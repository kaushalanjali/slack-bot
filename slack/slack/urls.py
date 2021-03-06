"""slack URL Configuration

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
# slack/urls.pyfrom django.conf.urls import url
from django.contrib import admin
from events.views import Events  
from django.conf.urls import url   
from rest_framework.response import Response
from slack import urls as slack_urls 


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^events/', Events.as_view()),
    url(r'^events/userpost', Events.as_view()),

                        
]