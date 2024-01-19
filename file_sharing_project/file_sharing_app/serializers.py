from rest_framework import serializers
from .models import CustomUser, File


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'roles', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'








# from rest_framework import serializers
# from .models import CustomUser, File
# from django.core.mail import send_mail
# from django.conf import settings



# ############################################ custom user serializer ####################################################################
# class CustomUserSerializer(serializers.ModelSerializer):
#     file_upload = serializers.FileField(allow_empty_file=False, write_only=True, required=False)
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'roles', 'password', 'file_upload']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(**validated_data)
#         return user
    

# ############################################ client user serializer ####################################################################
# class ClientUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['id', 'email', 'roles', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(**validated_data)

#         # Send email with encrypted URL
#         # Check if user is client 
#         encrypted_url = self.generate_encrypted_url(user)
#         send_mail(
#             'Welcome to File Sharing',
#             f'Thank you for signing up! Your encrypted URL is: {encrypted_url}',
#             settings.DEFAULT_FROM_EMAIL,
#             [user.email],
#             fail_silently=False,
#         )
#         return user

#     def generate_encrypted_url(self, user):
#         # here logic to generate and encrypt the URL here
#         # For simplicity, let's assume the URL is just the user's email for demonstration purposes.
#         encrypted_url = f'https://example.com/encrypted-url/{user.email}'
#         return encrypted_url


# class FileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = File
#         fields = '__all__'
