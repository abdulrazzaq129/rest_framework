from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import ValidationError

class RegisterSerializers(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ["username","email","password","password_confirmation"]

    def save(self):
        password = self.validated_data['password']
        password_confirmation = self.validated_data['password_confirmation']

        if password != password_confirmation:
            raise ValidationError({'error':'password is not same'})
        if User.objects.filter(email = self.validated_data['email']).exists():
            raise ValidationError({'error':'email already exists'})
        
        account = User(username = self.validated_data['username'], email = self.validated_data['email'])
        account.set_password(password)
        account.save()

        return account