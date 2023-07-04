from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from .authentication import TokenAuthenticationCustom

class AuthenticationCustom(object):
    user,token = None,None

    def get_user(self,request):
        """
        return:
            * user: Instace User that sended request
        """
        token = None
        try:
            token = get_authorization_header(request).split()[1].decode()
            self.token = token
        except:
            return None
        
        token_auth = TokenAuthenticationCustom()
        user = token_auth.authenticate_credentials(key=token)
        self.user = user

        if user != None and token != None:
            return user
    
    def dispatch(self,request,*args, **kwargs):
        user = self.get_user(request)
        print(user)

        if user:
            return super().dispatch(request,*args, **kwargs)
        
        response = Response(
            {
                'error':'usuario no autorizado'
            },
            status = status.HTTP_401_UNAUTHORIZED
        )

        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        
        return response
