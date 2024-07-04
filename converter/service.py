import json
import os


def get_filename(path: str) -> str:
    """ function getting filename from path """
    return path.split('/')[-1]


def new_file_local_path(path: str, output_format: str) -> str:
    """ function getting new local file path """
    filename = get_filename(path)
    filename_list = filename.split('.')
    new_filename = f"{filename_list[0]}.{output_format}"
    new_file_path = f"{os.path.dirname(path)}/{new_filename}"
    return new_file_path


def parse_flags(rule):
    """ function getting rule flags properly"""
    input = next(iter(rule.keys()))
    result_flags = ' '.join(rule[input]["flags"])
    return result_flags


def parse_flags_for_list(rule: dict):
    """ Rudimentary function for list command """
    input = next(iter(rule.keys()))
    result_flags = []
    for flag in rule[input]["flags"]:
        flag_list = flag.split(' ')
        result_flags.extend(flag_list)
    return result_flags


def new_file_minio_path(path: str, filename:str) -> str:
    """ function getting new minio file path """
    # input = next(iter(rule.keys()))
    # output_format = rule[input]["output"]
    # filename = get_filename(path)
    # filename_list = filename.split('.')
    # new_filename = f"{filename_list[0]}.{output_format}"
    new_file_path = f"{os.path.dirname(path)}/{filename}"
    return new_file_path


def delete_files_with_same_name_but_different_extension(file_path: str) -> None:
    """ buffer cleaner """
    directory = os.path.dirname(file_path)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    files_to_delete = [file for file in os.listdir(directory) if file.startswith(file_name) and os.path.isfile(os.path.join(directory, file))]
    for file in files_to_delete:
        os.remove(os.path.join(directory, file))


def get_new_minio_filename(local_path: str) -> str:
    """ function for getting a new filename for a file in minio (filename + _converted + .*new_format*)"""
    name, format = os.path.splitext(os.path.basename(local_path))
    final_minio_name = name.split('_')[0] + "_converted" + format
    return final_minio_name
