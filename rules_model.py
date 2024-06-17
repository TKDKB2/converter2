from functools import wraps
import json
import api.settings as settings


def singleton(cls):

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = cls(*args, **kwargs)
        return cls._instance

    return wrapper


@singleton
class Rules:

    # reading rules from json
    @staticmethod
    def read_json_file(file_path: str) -> dict:
        try:
            with open(file_path, "r") as file:
                json_data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error reading JSON file: {e}")
            json_data = {}
        except FileNotFoundError as e:
            print(f"Error opening file: {e}")
            json_data = {}

        return json_data

    # writing rules to json
    @staticmethod
    def write_json_file(file_path: str, data: dict):
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as e:
            print(f"Error writing to file: {e}. The specified file path was not found.")
        except (IOError, OSError) as e:
            print(f"Error writing to file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    # initialization of singletone by reading all rules from json
    def __init__(self):
        self._rules: dict = self.read_json_file(settings.JSON_RULES_PATH)
        print("INIT", self._rules)

    # creating the rule and updating json
    def create_rule(self, input_format, details):
        if input_format in self._rules:
            print("hello")
            print(self._rules)
            return f"Rule with input format '{input_format}' already exists"
        self._rules[input_format] = details
        self.write_json_file(settings.JSON_RULES_PATH, self._rules)
        print("aaaa", self._rules)
        return f"{self._rules}"

    # reading the rule
    def read_rule(self, input_format):
        if not self._rules.get(input_format):
            return "Rule not found"
        else:
            return {input_format: self._rules[input_format]}

    # reading all the rules
    def read_all_rules(self):
        return self._rules

    # updating the rule and updating json
    def update_rule(self, input_format, new_details):
        if input_format not in self._rules:
            return f"Rule with input format '{input_format}' does not exist"
        self._rules[input_format] = new_details
        self.write_json_file(settings.JSON_RULES_PATH, self._rules)
        return f"Rule with input format '{input_format}' updated successfully"

    # deleting the rule and updating json
    def delete_rule(self, input_format):
        if input_format not in self._rules:
            return f"Rule with input format '{input_format}' does not exist"
        del self._rules[input_format]
        self.write_json_file(settings.JSON_RULES_PATH, self._rules)
        return f"Rule with input format '{input_format}' deleted successfully"