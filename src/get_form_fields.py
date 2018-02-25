"""
Parse the form HTML into nice markdown

Input:
- *.txt file output from login.py

Output:
- *.json file containing question info as input for create_markdown.py
"""

import json

from bs4 import BeautifulSoup, NavigableString

# inputs
text_file = '../out/yc_app.txt'

# read text file containing URL of application page
with open(text_file, 'rb') as infile:
    html_src = infile.read()

# get main form
soup = BeautifulSoup(html_src, 'html.parser')
main_form = soup.form

# list of relevent form attributes
potential_attibutes = ['name', 'id']

# set limit for how far back from an element to search for its description
num_previous_element_limit = 10

questions_info = []

# get all inputs
# NOTE: all text areas have name and id parameters
for input_field in main_form.find_all(['textarea']):

    question_info = {}

    # get name and id of the element
    question_info = {
        potential_attibute: input_field[potential_attibute]
        for potential_attibute in potential_attibutes
        if potential_attibute in input_field.attrs
    }

    """
    find the description before the element
    - lazy way is to use input_field.previous_element
    - correct way is to find the matching "<label for='<...>'"
       for the element id
    """
    for_label = input_field['id']
    description = [
        e.text
        for e in main_form.find_all('label')
        if 'for' in e.attrs
        if e['for'] == for_label
    ][0]
    description_text = description.replace('\n', ' ')
    question_info['description'] = description_text

    questions_info.append(question_info)

# record questions info dictionary to JSON
questions_info_path = '../out/questions_info.json'
with open(questions_info_path, 'w') as outfile:
    json.dump(questions_info, outfile)
