from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from email_validator.utils import (
    is_valid_email_format,
    check_mx_record,
    check_smtp,
    check_spf,
    check_dkim,
    check_dmarc
)
from email_validator.models import EmailValidationResult

class EmailValidationAPIView(APIView):

    """POST endpoint to validate multiple emails and store results in DB."""

    def post(self, request):
        emails = request.data.get("emails", [])
        if not isinstance(emails, list):
            return Response({"error": "Emails must be a list"}, status=status.HTTP_400_BAD_REQUEST)

        results = []

        for email in emails:
            obj, created = EmailValidationResult.objects.get_or_create(email=email)

            if not created:
                results.append({
                    "email": obj.email,
                    "is_format_valid": obj.is_format_valid,
                    "has_mx": obj.has_mx,
                    "smtp_valid": obj.smtp_valid,
                    "spf": obj.spf,
                    "dkim": obj.dkim,
                    "dmarc": obj.dmarc,
                    "checked_at": obj.checked_at
                })
                continue

            obj.is_format_valid = is_valid_email_format(email)

            if obj.is_format_valid:
                domain = email.split("@")[1]
                obj.has_mx = check_mx_record(domain)
                obj.smtp_valid = check_smtp(email)
                obj.spf = check_spf(domain)
                obj.dkim = check_dkim(domain)
                obj.dmarc = check_dmarc(domain)
            else:
                obj.has_mx = False
                obj.smtp_valid = False
                obj.spf = False
                obj.dkim = False
                obj.dmarc = False

            obj.save()

            results.append({
                "email": obj.email,
                "is_format_valid": obj.is_format_valid,
                "has_mx": obj.has_mx,
                "smtp_valid": obj.smtp_valid,
                "spf": obj.spf,
                "dkim": obj.dkim,
                "dmarc": obj.dmarc,
                "checked_at": obj.checked_at
            })

        return Response(results, status=status.HTTP_200_OK)
