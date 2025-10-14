from django.db import models

class EmailValidationResult(models.Model):
    email = models.EmailField(unique=True)
    is_format_valid = models.BooleanField(default=False)
    has_mx = models.BooleanField(default=False)
    smtp_valid = models.BooleanField(default=False)
    spf = models.BooleanField(default=False)
    dkim = models.BooleanField(default=False)
    dmarc = models.BooleanField(default=False)
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
