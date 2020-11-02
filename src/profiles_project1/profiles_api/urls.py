from django.urls import path
from django.conf.urls import include

from rest_framework.routers import DefaultRouter
from rest_framework import authtoken
#from rest_framework.authtoken.views import obtain_auth_token


from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, basename='login')

urlpatterns = [
     path('hello-view/',views.HelloApiView.as_view()),
     path('', include(router.urls)),
     #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]
