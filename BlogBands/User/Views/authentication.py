from datetime import datetime
from rest_framework.views import APIView
from django.contrib.sessions.models import Session
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from User.serializers import UserSerializer
from User.autorization_mixin import AuthenticationCustom

class Login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data=request.data, context={'request':request})
        if login_serializer.is_valid(): #There is user in the database
            user = login_serializer.validated_data['user']
            user_serializer = UserSerializer(user)
            if user.is_active:
                token,created = Token.objects.get_or_create(user=user)
                if created:
                    return Response(
                        {
                            'token': token.key,
                            'user': user_serializer.data,
                            'message': 'All good'
                        },
                        status= status.HTTP_200_OK
                    )
                else:
                    token.delete()
                    return Response(
                        {
                            'message': 'you logged in'
                        },
                        status= status.HTTP_409_CONFLICT
                    )
            else:
                return Response({'Error':'El usuario no puede iniciar sesión'})
        else:
            return Response({'Error':'Nombre de usuario o contraseña incorrectos'})
        return Response({'message': 'Hola desde Login'})


class Logout(APIView, AuthenticationCustom ):
    def post(self, request):
        try:
            token = Token.objects.filter(key=request.data['token']).first()
            print(request.data['token'])
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte=datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message ='Sesiones de usuario eliminadas.'
                token_message = 'Token eliminado'
                return Response(
                {
                    'token_message': token_message,
                    'session_message': session_message,
                },
                status= status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        'error': 'No se ha encontrado un usuario con estas credenciales'
                    },
                    status= status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {
                    'error': 'Variable token no encontrada'
                },
                status= status.HTTP_409_CONFLICT
            )