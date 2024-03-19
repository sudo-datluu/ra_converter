from .models import FileUpload, Column
from .infer_data_types import infer_and_convert_data_types
import pandas as pd
from celery import shared_task

@shared_task
def process_file_task(file_upload_id: int):
    file_upload = FileUpload.objects.get(pk=file_upload_id)
    if not file_upload: return
    df = pd.read_csv(file_upload.content.path)
    infer_and_convert_data_types(df)
    for col, dtype in df.dtypes.items():
        column = Column(file=file_upload, column_type=dtype, name=col)
        column.save()