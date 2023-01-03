from django.contrib.auth.models import update_last_login
from rest_framework_simplejwt.tokens import RefreshToken


def get_jwt_tokens_for_user(user, update_user_last_login=False):
    refresh = RefreshToken.for_user(user)

    if update_user_last_login:
        update_last_login(None, user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }