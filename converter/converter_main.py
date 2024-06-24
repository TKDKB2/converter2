from download_upload_clean import download_video_from_minio, upload_video_to_minio
from convert import get_needed_rule, convert_video, convert, command_from_rule, command_from_message
from service import new_file_minio_path, get_filename, delete_files_with_same_name_but_different_extension
from datetime import datetime
from incoming_message_handler import handle_incoming_message


# test_minio_path = "/test_folder/sample-jpg-file-for-testing.jpg"


def main_worker(message: str):
    start_time = datetime.now()
    print("start", start_time)
    dict_message = handle_incoming_message(message)
    print(type(dict_message), dict_message)
    minio_path = dict_message["path"]
    local_video_path = download_video_from_minio(minio_path)
    # print(local_video_path)
    if dict_message["flags"] or dict_message["output"]:
        print("command from message")
        command, new_local_file_path = command_from_message(dict_message, local_video_path)
    else:
        print("command from rule")
        rule = get_needed_rule(local_video_path)
        command, new_local_file_path = command_from_rule(rule, local_video_path)
    convert(command)
    # new_local_file_path = convert_video(local_video_path, rule)
    new_minio_filename = get_filename(new_local_file_path)
    new_minio_path = new_file_minio_path(minio_path, new_minio_filename)
    # print(new_minio_path)
    upload_video_to_minio(new_minio_path)
    delete_files_with_same_name_but_different_extension(local_video_path)
    end_time = datetime.now()
    print("end", end_time)
    total_time = end_time - start_time
    print("total", total_time)



# main_worker(test_minio_path)


