from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from django.core.validators import ValidationError as DjangoValidationError


class IranMobilePhoneNumberValidator(RegexValidator):
    regex = '^(\+98)9\d{9}$'
    message = _('Please Enter a valid mobile number.')


def validate_mobile_number(mobile_number):
    validate = IranMobilePhoneNumberValidator()
    try:
        validate(mobile_number)
    except DjangoValidationError as e:
        raise ValidationError({"mobile": [e.message]})