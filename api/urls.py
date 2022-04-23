from django import urls
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from semester import views as semesterViews
from project import views as projectViews
from team import views as teamViews
from criteria import views as criteriaView
from evaluation import views as evaluationView
from judge import views as judgeView

router = SimpleRouter()
# basename='MyModel'
router.register('semester', semesterViews.SemesterViewSet, basename='semester')
router.register('project', projectViews.ProjectViewSet)
router.register('team', teamViews.TeamViewSet)
router.register('criteria', criteriaView.CriteriaViewSet)
router.register('evaluation', evaluationView.EvaluationViewset)
router.register('judge', judgeView.JudgeViewset)
# print(router.urls)

urlpatterns=[
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
    path('',include(router.urls))
]
