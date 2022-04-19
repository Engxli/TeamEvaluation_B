from django import urls
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from semester import views as semesterViews
from project import views as projectViews
from team import views as teamViews

router = SimpleRouter()
router.register('semester', semesterViews.SemesterViewSet)
router.register('project', projectViews.ProjectViewSet)
router.register('team', teamViews.TeamViewSet)
# print(router.urls)

urlpatterns=[
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
    path('',include(router.urls))
]
