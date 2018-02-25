"""
Fill out the YC Application.
NOTE: a big portion of this code is shared with login.py

Input:
- *.json file containing answers to questions from running answers_to_json.py

Output:
- no local output; instead, this fills out the online form
"""


import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, InvalidElementStateException

# inputs
config_path = '../input/config.json'
with open(config_path, 'r') as infile:
    config = json.load(infile)

login_url = config['login_url']
app_url = config['app_url']
text_file = config['text_file']

# read user credentials for login
credentials_path = '../input/credentials.json'
with open(credentials_path, 'r') as infile:
    credentials = json.load(infile)

# make new browser window
browser = webdriver.Firefox()
browser.get(login_url)

# enter username and password
for field in credentials['fields']:
    elem_name = credentials['fields'][field]['name']
    elem_value = credentials['fields'][field]['value']
    input_elem = browser.find_element_by_name(elem_name)
    input_elem.send_keys(elem_value)
    time.sleep(1)

# submit form
submit_btn = browser.find_element_by_xpath(credentials['submit']['xpath'])
submit_btn.click()

# go to app url
browser.get(app_url)

time.sleep(2)

"""
Part 2: fill in the form answers
"""
# read the json dictionary of questions and responses
form_answers_path = '../out/form_answers.json'
with open(form_answers_path, 'r') as infile:
    form_answers = json.load(infile)

for field in form_answers:
    if 'answer' not in field.keys():
        continue

    # probably best to use xpath with both name and id for textareas
    field_xpath = (
        "//textarea[@name='" +
        field['name']+
        "' and @id='" +
        field['id']+
        "']"
    )
    field_elem = browser.find_element_by_xpath(field_xpath)
    try:
        # don't use browser.clear()
        # NOTE: for Windows, may need to use Keys.CONTROL and not Keys.COMMAND
        field_elem.send_keys(Keys.COMMAND + "a");
        field_elem.send_keys(Keys.DELETE);
        field_elem.send_keys(field['answer'])
        time.sleep(0.25)
    except ElementNotInteractableException, InvalidElementStateException:
        continue

# save for later
save_xpath = "//button[@class='btn apply savelater']"
save_elem = browser.find_element_by_xpath(save_xpath)
save_elem.click()

time.sleep(2)

# close the browser
browser.close()
