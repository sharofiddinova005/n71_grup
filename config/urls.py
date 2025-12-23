"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
    openapi.Info(
        title="Serializer",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),

)



from django.urls import path, include
from configapp.views import ActorAPI, CommitAPI, MovieAPI, CommitApiView, SendEmailApi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'actor',ActorAPI)
router.register(r'commit',CommitAPI)
router.register(r'movie',MovieAPI)
# router.register(r'sendemail',SendEmailApi)
urlpatterns = [
    path('',include(router.urls)),
    path('commit_post/',CommitApiView.as_view()),
    path('commit_post/',SendEmailApi.as_view()),
    # path('category/',CategoryAPi.as_view()),
    # path('category/<int:pk>/',CategoryDetailAPi.as_view()),

]
