"""
Login and get page contents

Output:
- *.txt file that is used as input to get_form_fields.py
"""

import json
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

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

# get page contents
html_src = browser.page_source

# close window
browser.close()

# store in text file
with open(text_file, 'wb') as outfile:
    outfile.write(html_src.encode('utf-8'))
