from django.urls import path

from apps.authn import views

urlpatterns = [
    path('auth/signin', views.SignIn.as_view(), name='authn-signin'),
    path('auth/signout', views.SignOut.as_view(), name='authn-signout'),
]
