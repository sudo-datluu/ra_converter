from rest_framework.response import Response
from rest_framework.decorators import action
from .models import FileUpload, Column
from .serializers import FilesSerializer, ColumnSerializer
from rest_framework import viewsets, status
from .infer_data_types import infer_and_convert_data_types
import pandas as pd
import asyncio

class FilesViewSet(viewsets.ModelViewSet):
    queryset = FileUpload.objects.all()
    serializer_class = FilesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            file_upload = serializer.save()
            # asyncio.create_task(self.process_file(file_upload))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # process each column
    async def process_file(self, file_upload):
        df = pd.read_csv(file_upload.file.path)
        infer_and_convert_data_types(df)
        for col, dtype in df.dtypes.items():
            column = Column(file=file_upload, column_type=dtype, name=col)
            column.save()

class ColumnViewSet(viewsets.ModelViewSet):
    serializer_class = ColumnSerializer

    def get_queryset(self):
        return Column.objects.all()
    
    @action(detail=True, methods=['get'])
    def columns(self, request, pk=None):
        file_id = self.kwargs['pk']
        columns = Column.objects.filter(file__id=file_id)
        serializer = self.get_serializer(columns, many=True)
        return Response(serializer.data)