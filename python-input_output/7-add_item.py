#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    # Try to load existing list from file
    items = load_from_json_file(filename)
except FileNotFoundError:
    # Initialize empty list if file does not exist
    items = []

# Add all command line arguments starting from index 1
items.extend(sys.argv[1:])

# Save the updated list back to the file
save_to_json_file(items, filename)
