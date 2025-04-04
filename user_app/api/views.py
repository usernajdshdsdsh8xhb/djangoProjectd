

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from user_app.api.serializers import RegistrationSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            user = User.objects.get(email=request.data["email"], password = request.data["password"])
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'email': user.email,
                'name': user.first_name,
                'token': token.key,
            })
        except:
            return Response({"message": "An Error Happened"})


@api_view(["POST"])
def registration_view(request):
    try:
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["name"] = account.first_name
            data["email"] = account.email
            token = Token.objects.get_or_create(user=account)[0].key
            data["token"] = token
            return Response(data)
        else:
            data = serializer.errors
    except:
        return Response({"message":'An Error Happened'})
    