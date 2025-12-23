from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from configapp.views import ActorAPI, SendEmailApi
from rest_framework.routers import DefaultRouter
from configapp.views import CommitAPI, MovieAPI, CommitApiView

router = DefaultRouter()
router.register(r'actor',ActorAPI)
router.register(r'commit',CommitAPI)
router.register(r'movie',MovieAPI)
router.register(r'sendemail',SendEmailApi)
urlpatterns = [
    path('',include(router.urls)),
    path('commit_post/',CommitApiView.as_view()),
    path('commit_post/',SendEmailApi.as_view()),
    # path('category/',CategoryAPi.as_view()),
    # path('category/<int:pk>/',CategoryDetailAPi.as_view()),
]

