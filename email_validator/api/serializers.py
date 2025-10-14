from rest_framework import serializers
from email_validator.models import EmailValidationResult

class EmailValidationResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailValidationResult
        fields = "__all__"
