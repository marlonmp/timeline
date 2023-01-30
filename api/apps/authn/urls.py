from django.urls import path

from apps.authn import views as v

urlpatterns = [
    path('auth/signin', v.SignIn.as_view(), name='authn-signin'),
    path('auth/signout', v.SignOut.as_view(), name='authn-signout'),
]
