from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import CustomUserSerializer


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)

        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = "Registration Successful"
            data['username'] = account.username
            data['email'] = account.email

            # JWT
            refresh = RefreshToken.for_user(user=account)
            data['token'] = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        else:
            data = serializer.errors
        return Response(data)

