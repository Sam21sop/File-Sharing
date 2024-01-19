from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, File
from .serializers import UserSerializer, FileSerializer



class UserRegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            token = {'refresh': str(refresh), 'access': str(refresh.access_token)}
            return Response({'token': token, 'user_id': user.id}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            token = {'refresh': str(refresh), 'access': str(refresh.access_token)}
            return Response({'token': token, 'user_id': user.id}, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class FileUploadView(APIView):
    def post(self, request, *args, **kwargs):
        # file upload logic here
        # Make sure to associate the uploaded file with the logged-in user
        return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)


class FileDownloadView(APIView):
    def get(self, request, file_id, *args, **kwargs):
        # file download logic here
        # Ensure that only authenticated users can download files
        return Response({'message': 'File downloaded successfully'}, status=status.HTTP_200_OK)


class GetAllUploadFilesView(APIView):
    def get(self, request, *args, **kwargs):
        # logic to get all uploaded files
        # Ensure that only authenticated users can get all files
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



















# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from .models import CustomUser, File
# from .serializers import CustomUserSerializer, ClientUserSerializer, FileSerializer
# from django.shortcuts import get_object_or_404
# import magic

# ################################################## operation signup/login ############################################################################

# class SignupView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()

#             # Check file type before saving
#             uploaded_file = request.FILES.get('file_upload')
#             if uploaded_file:
#                 file_type = magic.Magic()
#                 file_mime_type = file_type.from_buffer(uploaded_file.read(1024))
#                 if not file_mime_type.startswith(('application/vnd.openxmlformats-officedocument', 'application/msword')):
#                     # user.delete()  # Remove user if file type is invalid
#                     return Response({'detail': 'Invalid file type'}, status=status.HTTP_400_BAD_REQUEST)

#             refresh = RefreshToken.for_user(user)
#             token = {'refresh': str(refresh), 'access': str(refresh.access_token)}
#             return Response({'token': token, 'user_id': user.id}, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = CustomUser.objects.filter(email=email).first()

#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             token = {'refresh': str(refresh), 'access': str(refresh.access_token)}
#             return Response({'token': token, 'user_id': user.id}, status=status.HTTP_200_OK)
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# ################################################## Client signup/login ############################################################################

# class ClientSignupView(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = ClientUserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             refresh = RefreshToken.for_user(user)
#             token = {'refresh': str(refresh), 'access': str(refresh.access_token)}
#             return Response({'token': token, 'user_id': user.id}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class EmailVerifyView(APIView):
#     def get(self, request, email_token, *args, **kwargs):
#         user = get_object_or_404(CustomUser, email=email_token, is_active=False)
#         user.is_active = True
#         user.save()
#         serializer = ClientUserSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)


# class LoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = CustomUser.objects.filter(email=email).first()

#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             token = {'refresh': str(refresh), 'access': str(refresh.access_token)}
            
#             if user.is_client():
#                 client_serializer = ClientUserSerializer(user)
#                 return Response({'token': token, 'user': client_serializer.data}, status=status.HTTP_200_OK)
#             else:
#                 return Response({'detail': 'Only client users can log in'}, status=status.HTTP_403_FORBIDDEN)
        
#         return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class ClientDownloadView(APIView):
#     def get(self, request, file_id, *args, **kwargs):
#         # file = get_object_or_404(File, id=file_id)
        
#         if request.user.is_authenticated and request.user.is_client():
#             # logic to generate the secure download link
#             secure_download_link = f'https://example.com/download-file/{file_id}/token123'
            
#             # logic to respond with the secure download link
#             return Response({'download-link': secure_download_link, 'message': 'success'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)


# class OpsGetAllFilesView(APIView):
#     def get(self, request, *args, **kwargs):
#         if request.user.is_authenticated and 'ops' in request.user.roles.lower():
#             files = File.objects.all()
#             serializer = FileSerializer(files, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'detail': 'Access denied'}, status=status.HTTP_403_FORBIDDEN)
