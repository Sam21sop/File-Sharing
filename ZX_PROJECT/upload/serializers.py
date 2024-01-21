from rest_framework.serializers import FileField, ListField, Serializer




class UploadSerializer(Serializer):
    ''' Single file upload serializer '''
    upload_file = FileField()
    class Meta:
        fields = ['upload_file']


class MultiFileUploadSerializer(Serializer):
    ''' Multiple Files upload Serialiser '''
    upload_files = ListField()
    class Meta:
        fields = ['upload_files']
