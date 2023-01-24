from django.contrib.auth import authenticate, login, logout

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.permissions import IsAuthenticated

from apps.authn.serializers import UserCredentials


class SignIn(APIView):

    authentication_classes = ()

    def post(self, request):
        serializer = UserCredentials(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(request, **serializer.data)
        
        if user is None:
            raise AuthenticationFailed()

        login(request, user)

        return Response(status=status.HTTP_202_ACCEPTED)


class SignOut(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_202_ACCEPTED)
