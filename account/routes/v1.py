from django.urls import path


from account.views import (
    VerifyByMobileOTPCodeAPIView,
    LoginByMobileOTPCodeAPIView
)

urlpatterns = [
    path('login/', LoginByMobileOTPCodeAPIView.as_view(), name='login'),
    path('verify/', VerifyByMobileOTPCodeAPIView.as_view(), name='verify')
]