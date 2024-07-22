#Things to remeber
import json
import os

# Write JSON to file
with open(file_path, 'w') as f:
    json.dump(message_dictionary, f)

# Read JSON from file
with open(file_path, 'r') as f:
    message_dictionary = json.load(f)

#Get current file directory
project_directory = os.path.dirname(os.path.abspath(__file__))

#Get user imput and prompt
print('Welcome to program')
user_input = input('Select language:' + '\n' + '1) English' + '\n' + '2) Spanish')
language_select = input()