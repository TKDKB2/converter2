import json

from rules_model import Rules
import subprocess
from service import get_filename, new_file_local_path, parse_flags, parse_flags_for_list
from settings import ROOT_BUFFER_DIR
from api.settings import JSON_RULES_PATH

rules = Rules()

def command_from_message(message: dict, video_file_local_path: str) -> tuple[str, str]:
    """ function to get ffmpeg command from message """
    new_local_file_path = new_file_local_path(video_file_local_path, message["output"])
    flags = ' '.join(message["flags"])
    command = f"ffmpeg -i {video_file_local_path} {flags} -loglevel quiet {new_local_file_path}"
    return command, new_local_file_path


def command_from_rule(rule: dict, video_file_local_path: str) -> tuple[str, str]:
    """ function to get ffmpeg command from rule """
    input = next(iter(rule.keys()))
    new_local_file_path = new_file_local_path(video_file_local_path, rule[input]["output"])
    flags = parse_flags(rule)
    command = f"ffmpeg -i {video_file_local_path} {flags} -loglevel quiet {new_local_file_path}"
    return command, new_local_file_path


def convert(command: str):
    """ convertion """
    subprocess.run(command, shell=True)


# """ Converting the video """
# def convert_video(video_file_local_path, rule):
#     input = next(iter(rule.keys()))
#     filename = get_filename(video_file_local_path)
#     # print(rule[input])
#     new_local_file_path = new_file_local_path(video_file_local_path, rule[input]["output"])
#     # flags = parse_flags_for_list(rule)
#     # command = []
#     # command.extend(["ffmpeg", "-i", video_file_local_path])
#     # command.extend(flags)
#     # command.extend([new_local_file_path])
#     flags = parse_flags(rule)
#     command = f"ffmpeg -i {video_file_local_path} {flags} -loglevel quiet {new_local_file_path}"
#     # print(command)
#     subprocess.run(command, shell=True)
#     return new_local_file_path


def get_needed_rule(video_file_local_path: str) -> dict | set[str]:
    """ Getting a rule depending on a format """
    if not video_file_local_path:
        return {"message: no path"}
    video_format = video_file_local_path.split('.')[-1]
    try:
        with open(JSON_RULES_PATH, "r") as file:
            rules = json.load(file)
    except json.JSONDecodeError as e:
        print(f"Error reading JSON file: {e}")
        rules = {}
    except FileNotFoundError as e:
        print(f"Error opening file: {e}")
        rules = {}

    try:
        meta = rules[video_format]
        print(meta)
        rule = {video_format: meta}
        return rule
    except KeyError:
        return {"message: no rule found for this video format"}
