from bank.models import users, BankDetails
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['id', 'username', 'email', 'password', 'created_at', 'updated_at']

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = ['id', 'user', 'account_number', 'account_type', 'balance', 'created_at', 'updated_at']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = users.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user