from users.models import CustomUser
from django.contrib.auth.models import User
from rest_framework import serializers


class CustomUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'error': 'both password should be same'})
        if CustomUser.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'email already exist'})
        account = CustomUser(email=self.validated_data['email'], username=self.validated_data['username'],
                             first_name=self.validated_data['first_name'],
                             last_name=self.validated_data['last_name'])
        account.set_password(password)
        account.save()
        return account
