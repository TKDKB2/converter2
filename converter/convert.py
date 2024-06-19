import ffmpeg
from rules_model import Rules
import subprocess
from service import get_filename, new_file_local_path, parse_flags, parse_flags_for_list
from settings import ROOT_BUFFER_DIR

rules = Rules()

""" Converting the video """
def convert_video(video_file_local_path, rule):
    input = next(iter(rule.keys()))
    filename = get_filename(video_file_local_path)
    print(rule[input])
    new_local_file_path = new_file_local_path(video_file_local_path, rule[input]["output"])
    flags = parse_flags_for_list(rule)
    # command = []
    # command.extend(["ffmpeg", "-i", video_file_local_path])
    # command.extend(flags)
    # command.extend([new_local_file_path])
    flags = parse_flags(rule)
    command = f"ffmpeg -i {video_file_local_path} {flags} {new_local_file_path}"
    print(command)
    subprocess.run(command, shell=True)
    return new_local_file_path


""" Getting a rule depending on a format """
def get_needed_rule(video_file_local_path):
    video_format = video_file_local_path.split('.')[-1]
    try:
        rule = {video_format: rules._rules[video_format]}
        return rule
    except KeyError:
        return {"message: no rule found for this video format"}


# rule = get_needed_rule(f"{ROOT_BUFFER_DIR}/sample-5s.mp4")
# convert_video(f"{ROOT_BUFFER_DIR}/sample-5s.mp4", rule)