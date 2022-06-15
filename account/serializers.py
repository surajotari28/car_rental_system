from rest_framework import serializers
from . models import User


class UserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'phonenumber', 'address', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phonenumber',
                  'address', 'password', 'confirm_password']

# Validating Password and Confirm Password while Registration

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError(
                "Password and Confirm Password doesn't match")
        return attrs

    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name',
                  'last_name', 'phonenumber', 'address']
