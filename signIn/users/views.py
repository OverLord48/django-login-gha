from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from users.serializer import LoginUserSerializer, CreateUserSerializer
from users.services import logout_token

# Create your views here.

class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer
    http_method_names = ['post']
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


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


class LogoutView(APIView):
    def post(self, request):
        # enviamos el token recibido por form-data al microservicio
        logout_token(request.data.get("token"))
        # Devolvemos la respuesta al cliente
        return Response({'success': True,'status':status.HTTP_200_OK})
