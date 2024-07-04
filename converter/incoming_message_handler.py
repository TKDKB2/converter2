import json


def handle_incoming_message(message: str) -> dict:
    """ function for getting dict from incoming json message """
    try:
        dict_message = json.loads(message)
        return dict_message
    except Exception as e:
        return e
