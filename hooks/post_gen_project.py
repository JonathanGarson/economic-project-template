# thanks to Audrey Feldroy for this hook

import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

# Remove file if licence is == "Not open source"
if __name__ == '__main__':
    if '{{ cookiecutter.open_source_license }}' == 'Not open source':
        remove_file('LICENSE')