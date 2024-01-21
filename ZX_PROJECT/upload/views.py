from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer



class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer


    def list(self, request):
        return Response("GET API: You Received Encrypted URL")
    

    def create(self, request):
        file_uploaded = request.FILES.get('upload_file')
        content_type = file_uploaded.content_type
        return Response(f'POST API: Files Uploaded Successfully.')