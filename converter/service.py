import os

""" function getting filename from path """
def get_filename(path: str) -> str:
    return path.split('/')[-1]


""" function getting new local file path """
def new_file_local_path(path: str, output_format: str) -> str:
    filename = get_filename(path)
    filename_list = filename.split('.')
    new_filename = f"{filename_list[0]}.{output_format}"
    new_file_path = f"{os.path.dirname(path)}/{new_filename}"
    return new_file_path


""" function getting rule flags properly"""
def parse_flags(rule):
    input = next(iter(rule.keys()))
    result_flags = ' '.join(rule[input]["flags"])
    print(result_flags)
    return result_flags


""" Rudimentary function for list command """
def parse_flags_for_list(rule: dict):
    input = next(iter(rule.keys()))
    result_flags = []
    for flag in rule[input]["flags"]:
        flag_list = flag.split(' ')
        result_flags.extend(flag_list)
    print(result_flags)
    return result_flags


""" function getting new minio file path """
def new_file_minio_path(path: str, filename:str, rule) -> str:
    input = next(iter(rule.keys()))
    output_format = rule[input]["output"]
    # filename = get_filename(path)
    # filename_list = filename.split('.')
    # new_filename = f"{filename_list[0]}.{output_format}"
    new_file_path = f"{os.path.dirname(path)}/{filename}"
    return new_file_path


""" buffer cleaner """
def delete_files_with_same_name_but_different_extension(file_path):
    directory = os.path.dirname(file_path)
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    files_to_delete = [file for file in os.listdir(directory) if file.startswith(file_name) and os.path.isfile(os.path.join(directory, file))]
    for file in files_to_delete:
        os.remove(os.path.join(directory, file))
        print(f"Файл {file} удален")