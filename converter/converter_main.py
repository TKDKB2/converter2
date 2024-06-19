from download_upload_clean import download_video_from_minio, upload_video_to_minio
from convert import get_needed_rule, convert_video
from service import new_file_minio_path, get_filename, delete_files_with_same_name_but_different_extension

test_minio_path = "/test_folder/sample-5s.mp4"


def main(minio_path: str):
    local_video_path = download_video_from_minio(test_minio_path)
    print("файл скачан")
    rule = get_needed_rule(local_video_path)
    print("правило получено")
    new_local_file_path = convert_video(local_video_path, rule)
    new_minio_filename = get_filename(new_local_file_path)
    print("видео сконвертировано")
    new_minio_path = new_file_minio_path(test_minio_path, new_minio_filename, rule)
    print(new_minio_path)
    upload_video_to_minio(new_minio_path)
    print("видео загружено")
    delete_files_with_same_name_but_different_extension(local_video_path)


main(test_minio_path)


