# Moduł data_utils - operacje na danych

import json

def json_to_dict(json_str):
    # Konwertuje JSON na słownik
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        return None

def dict_to_json(data_dict):
    # Konwertuje słownik na JSON
    return json.dumps(data_dict, indent=4)
