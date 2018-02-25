# YC Form Filler
NOTE: only fills text areas for now

### Script running order

1. `login.py`
2. `get_form_fields.py`
3. `create_markdown.py`
4. `answers_to_json.py`
5. `fill_form.py`

### Important

- Remember to edit the `credentials.json` file with your login info`
  - May also need to edit the `config.json`
- Remember to get GeckoDriver if using Firefox
  - Remember to add the path to the folder containing GeckoDriver in your
    bash profile
  - GeckoDriver currently comes in the project's `depends/` folder
