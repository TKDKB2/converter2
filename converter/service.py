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


