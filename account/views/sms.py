# from celery import shared_task
from django.conf import settings
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from rest_framework.views import APIView
from django.contrib.auth import get_user_model

from account.utils import get_jwt_tokens_for_user
from account.validators import validate_mobile_number

User = get_user_model()


# @shared_task
# def _remove_user_if_mobile_is_not_verified(user_id):
#     User.objects.filter(pk=user_id, is_mobile_verified=False).delete()

class LoginByMobileOTPCodeAPIView(APIView):
    @staticmethod
    def get_or_create_user_by_mobile(mobile):
        if User.objects.filter(mobile=mobile).exists():
            user = User.objects.get(mobile=mobile)
        else:
            user = User(mobile=mobile)
            user.set_unusable_password()
            user.save()

        return user

    def post(self, request, *args, **kwargs):
        request_data = request.data
        mobile = request_data.get('mobile', None)
        validate_mobile_number(str(mobile))
        user = self.get_or_create_user_by_mobile(mobile)
        response = user.send_otp_code_with_sms()
        # _remove_user_if_mobile_is_not_verified.apply_async(
        #     args=[user.id],
        #     countdown=settings.TIME_OTP_EXPIRE_INTERVAL,
        # )
        return Response(response, status=status.HTTP_201_CREATED)


class VerifyByMobileOTPCodeAPIView(APIView):
    def post(self, request, *args, **kwargs):
        request_data = self.request.data
        mobile = request_data.get('mobile', None)
        otp = request_data.get('otp', None)
        validate_mobile_number(mobile)
        user = get_object_or_404(
            queryset=User.objects.all(),
            mobile=mobile
        )

        if not user.verify_otp_code_sms(otp):
            return Response(
                data='please enter valid otp code',
                status=status.HTTP_401_UNAUTHORIZED,
            )

        if not user.is_mobile_number_verified:
            user.is_mobile_number_verified = True
            user.save()

        return Response(
            data=get_jwt_tokens_for_user(user=user, update_user_last_login=True),
            status=status.HTTP_200_OK,
        )
