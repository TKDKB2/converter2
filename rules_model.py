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

    @staticmethod
    def read_json_file(file_path: str) -> dict:
        """ reading rules from json """
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

    @staticmethod
    def write_json_file(file_path: str, data: dict):
        """ writing rules to json """
        try:
            with open(file_path, "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError as e:
            print(f"Error writing to file: {e}. The specified file path was not found.")
        except (IOError, OSError) as e:
            print(f"Error writing to file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def __init__(self):
        """ initialization of singletone by reading all rules from json """
        self._rules: dict = self.read_json_file(settings.JSON_RULES_PATH)
        print("INIT", self._rules)

    def create_rule(self, input_format, details):
        """ creating the rule and updating json """
        if input_format in self._rules:
            print("hello")
            print(self._rules)
            return f"Rule with input format '{input_format}' already exists"
        self._rules[input_format] = details
        self.write_json_file(settings.JSON_RULES_PATH, self._rules)
        print("aaaa", self._rules)
        return f"{self._rules}"

    def read_rule(self, input_format):
        """ reading the rule """
        if not self._rules.get(input_format):
            return "Rule not found"
        else:
            return {input_format: self._rules[input_format]}

    def read_all_rules(self):
        """ reading all the rules """
        return self._rules

    def update_rule(self, input_format, new_details):
        """ updating the rule and updating json """
        if input_format not in self._rules:
            return f"Rule with input format '{input_format}' does not exist"
        self._rules[input_format] = new_details
        self.write_json_file(settings.JSON_RULES_PATH, self._rules)
        return f"Rule with input format '{input_format}' updated successfully"

    def delete_rule(self, input_format):
        """ deleting the rule and updating json"""
        if input_format not in self._rules:
            return f"Rule with input format '{input_format}' does not exist"
        del self._rules[input_format]
        self.write_json_file(settings.JSON_RULES_PATH, self._rules)
        return f"Rule with input format '{input_format}' deleted successfully"