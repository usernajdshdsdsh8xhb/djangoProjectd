

from django.contrib.auth.models import User
from rest_framework import serializers

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["name","email","password", "telegramID"]
        extra_kwargs = {
            "password": {"write_only":True}
            ,"name":{"source":"first_name"}, "telegramID":{"source":"last_name"}
        }
        
    def save(self, **kwargs):
        return super().save(**kwargs, username=self.validated_data["first_name"])