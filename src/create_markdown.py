"""
Create a markdown file with headers for each question in the application

Input:
- *.json file from get_form_fields.py

Output:
- *.md file for manually filling in and tracking changes in the form
  passed to answers_to_json.py
"""

import json

# get the dictionary of form questions
questions_info_path = '../out/questions_info.json'
with open(questions_info_path, 'r') as infile:
    questions_info = json.load(infile)

file_string = ''

# parse the dictionary into a string
for question_info in questions_info:
    description_text = question_info['description']
    description_header = '### ' + description_text + '\n\n'
    file_string += description_header
    # print(description_header)

# markdown output
markdown_skeleton_path = '../out/app_skeleton_blank.md'
with open(markdown_skeleton_path, 'w') as outfile:
    outfile.write(file_string)
