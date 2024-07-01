import json
from convert import get_needed_rule



def handle_incoming_message(message: str):
    # print(type(message), message)
    dict_message = json.loads(message)
    # print(type(dict_message), dict_message)
    return dict_message
