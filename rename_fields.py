#!/usr/bin/env fbpython
# (c) Meta Platforms, Inc. and affiliates. Confidential and proprietary.

import re


def replace_field_names(file_path):
    with open(file_path, "r") as file:
        file_data = file.read()
    # Find all field names
    field_names = re.findall(r" (\w+);", file_data)
    # Create a mapping of old field names to new ones
    field_mapping = {name: f"field{i+1}" for i, name in enumerate(field_names)}
    # Replace all occurrences of the old field names
    for old_name, new_name in field_mapping.items():
        file_data = re.sub(rf" {old_name};", f" {new_name};", file_data)
    # Write the modified data back to the file
    with open(file_path, "w") as file:
        file.write(file_data)


replace_field_names("Bad.thrift")
