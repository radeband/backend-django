import base64
from datetime import datetime
from decouple import config
from django.conf import settings
import pyotp

from django.core.cache import cache

from kavenegar import *


class OTPKeyHelper:
    @staticmethod
    def get_encoded_base32(value: str):
        key = f'{value}-{datetime.date(datetime.now())}-{settings.SMS_SECRET_KEY}'
        return base64.b32encode(key.encode())


class OTPMixin:
    mobile: str = ''

    def _get_totp(self):
        key = OTPKeyHelper.get_encoded_base32(self.mobile).decode()
        return pyotp.TOTP(
            key,
            interval=settings.TIME_OTP_EXPIRE_INTERVAL
        )

    def _get_otp_code(self):
        totp = self._get_totp()
        code = totp.now()
        return code

    def send_otp_code_with_sms(self):
        # payload = f"message={self._get_otp_code()}&sender={config(config('SMS_PROVIDER')+'_SENDER')}&Receptor={self.mobile}"
        # headers = {
        #     'apikey': config(config('SMS_PROVIDER')+'_KEY'),
        #     'Accept': 'application/json'
        # }
        # response = requests.request("POST", config(config('SMS_PROVIDER') + '_URL'), data=payload, headers=headers)

        try:
            import json
        except ImportError:
            import simplejson as json
        try:
            api = KavenegarAPI(config('KAVENEGAR_KEY'))
            params = {
                'receptor': self.mobile,
                'token': self._get_otp_code(),
                'template': 'radeband'
            }
            
            response = api.verify_lookup(params)

        except APIException as e:
            print(str(e))

        except HTTPException as e:
            print(str(e))

        # response = requests.request("POST", config(config('SMS_PROVIDER' + '_URL')), data=payload, headers=headers)
        # return response.text


    def verify_otp_code_sms(self, code):
        totp = self._get_totp()
        return totp.verify(str(code))