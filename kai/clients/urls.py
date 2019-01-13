"""kai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from clients.views import  ClientListView, ClientCreateView, ClientDetailView

urlpatterns = [
    url(
        regex=r'^$',
        view=ClientListView.as_view(),
        name='client_list_api'
    ),
    url(
        regex=r'^detail/(?P<uuid>[-\w]+)/$',
        view=ClientDetailView.as_view(),
        name='client_detail_api'
    ),
    url(
        regex=r'^create/$',
        view=ClientCreateView.as_view(),
        name='client_create_api'
    )
]
