import os
import json

# Get the directory path of the current file (views.py)

def get_api():
        file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config.json')
        with open(file_path) as json_file:
                data = json.load(json_file)
        fetch = {
                "host": data['api_host'],
                "traffic": data['traffic'],
                "default_redirect_uri": data['default_redirect_uri']
                }
        return fetch
