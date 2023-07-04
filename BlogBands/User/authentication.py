from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class TokenAuthenticationCustom(TokenAuthentication):

    def authenticate_credentials(self, key):
        user = None
        try:
            token = self.get_model().objects.get(key=key)
            user = token.user
        except self.get_model().DoesNotExist:
           print('error')

        return user
