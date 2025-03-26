# Plik my_awesome_lib/__init__.py

from my_awesome_lib.data_utils import json_to_dict, dict_to_json
from my_awesome_lib.math_tools import factorial, is_prime
from my_awesome_lib.text_processing import reverse_text, count_words

__all__ = ["json_to_dict", "dict_to_json", "factorial", "is_prime", "reverse_text", "count_words"]
