import minio
import os
from service import get_filename, new_file_local_path
from settings import ROOT_BUFFER_DIR, BUCKET_NAME, MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, SSL_FLAG
import uuid


""" Connection to MINIO server """
minio_client = minio.Minio(
                           MINIO_ENDPOINT,
                           access_key=MINIO_ACCESS_KEY,
                           secret_key=MINIO_SECRET_KEY,
                           secure=SSL_FLAG
                           )


def download_video_from_minio(video_path: str) -> str:
    """ Download the video"""
    filename = get_filename(video_path)
    unique_id = str(uuid.uuid4())
    filename_list = filename.split('.')
    local_filename = f'{filename_list[0]}_{unique_id}.{filename_list[-1]}'
    minio_client.fget_object(f'{BUCKET_NAME}', f'{video_path}', f'{ROOT_BUFFER_DIR}/{local_filename}')
    return f'{ROOT_BUFFER_DIR}/{local_filename}'


def upload_video_to_minio(video_path: str, local_filepath: str) -> None:
    """ Upload the video"""
    filename = get_filename(local_filepath)
    minio_client.fput_object(f'{BUCKET_NAME}', f'{video_path}', f'{ROOT_BUFFER_DIR}/{filename}')








