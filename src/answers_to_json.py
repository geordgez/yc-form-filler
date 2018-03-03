"""
Convert completed Markdown form back into a JSON dictionary

Input:
- a completed markdown file based on the *.md output from create_markdown.py
  containing answers to each question section

Output:
- *.json file to be used to in fill_form.py
"""

import re
import json

# read markdown file
completed_form_path = '../out/app_draft_1.md'
with open(completed_form_path, 'r') as infile:
    completed_form = infile.read()

# read original questions JSON dictionary
questions_info_path = '../out/questions_info.json'
with open(questions_info_path, 'r') as infile:
    questions_info = json.load(infile)

# split into a list of questions and responses
answer_list = completed_form.split('###')
# print(answer_list)

# attach the answer to each question
for question_info in questions_info:

    # get the original question
    original_question = question_info['description'].strip()

    # print(original_question)

    # find the matching question-answer block from the completed form
    app_answer_list = [
        qa_block
        for qa_block in answer_list
        if original_question in qa_block
    ]

    # notify if the exact question wasn't found
    if not app_answer_list:
        print("".join([
            "Question not found -- did you delete or edit it?\n --> ",
            question_info['description'],
            "\n==============\n"
        ]))
        continue

    # store only the answer after removing leading and trailing whitespaces
    question_info['answer'] = app_answer_list[0].replace(
        original_question, ""
    ).replace(
        "\n\n", "<actual-line-break>"
    ).replace(
        "\n", " "
    ).replace(
        "<actual-line-break>", "\n\n"
    ).strip()

# write to local JSON
form_answers_path = '../out/form_answers.json'
with open(form_answers_path, 'w') as outfile:
    json.dump(questions_info, outfile)
