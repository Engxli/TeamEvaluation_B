from django import urls
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from semester import views as semesterViews


router = SimpleRouter()
router.register('semester', semesterViews.SemesterViewSet)
# print(router.urls)

urlpatterns=[
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
    path('',include(router.urls))
]
