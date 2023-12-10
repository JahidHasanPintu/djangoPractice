from rest_framework import serializers
from .models import LoanApplication
class LoanApplicationSerializers(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['id','applicantName','description']