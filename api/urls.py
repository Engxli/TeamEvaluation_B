from xml.etree.ElementInclude import include
from django.urls import path, include

urlpatterns=[
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt'))
]
