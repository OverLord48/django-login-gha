from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from users.serializer import LoginUserSerializer

# Create your views here.

class login(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data)
        if login_serializer.is_valid():
            user = login_serializer.validated_data["user"]
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                user_serializer = LoginUserSerializer(user).data
                if created:
                    return Response({
                        "token":token.key,
                        "user":user_serializer
                    }, status=status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user=user)
                    return Response({
                        "token":token.key,
                        "user":user_serializer
                    }, status=status.HTTP_201_CREATED)
            else:
                return Response({"error":"usuario inactivo"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"error":"nombre de usuario o clave incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"mensaje":"hola"}, status=status.HTTP_200_OK)