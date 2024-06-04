import os
import json


def read_json_file(file_name):
    absolute_path = os.path.join(os.getcwd(), file_name)

    with open(absolute_path, 'r') as f:
        return json.load(f)


def write_json_file(file_name, data):
    absolute_path = os.path.join(os.getcwd(), file_name)

    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)
