from django.db import models

class LoanApplication(models.Model):
    applicantName = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.applicantName + ' ' + self.description
    # mobile = models.PhoneNumberField(_("01"))
    # email = models.EmailField
    