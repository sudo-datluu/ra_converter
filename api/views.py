from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FileUpload, Column
from .serializers import FilesSerializer, ColumnSerializer
from rest_framework import viewsets, status
from .tasks import process_file_task

class FilesViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FilesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            file_upload = serializer.save()
            process_file_task.delay(file_upload_id=file_upload.fileID)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColumnViewSet(viewsets.ModelViewSet):
    serializer_class = ColumnSerializer

    def get_queryset(self):
        return Column.objects.all()
    
    # @action(detail=True, methods=['get'])
    def list(self, request, *args, **kwargs):
        file_id = self.kwargs['file_id']
        columns = Column.objects.filter(file__fileID=file_id)
        serializer = self.get_serializer(columns, many=True)
        return Response(serializer.data)