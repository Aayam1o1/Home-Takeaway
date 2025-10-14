from django.urls import path
from email_validator.api.views import EmailValidationAPIView

urlpatterns = [
    path("validate/", EmailValidationAPIView.as_view(), name="email-validate"),
]
