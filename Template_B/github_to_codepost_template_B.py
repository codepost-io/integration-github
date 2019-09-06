import requests
import json
import re
import os
import shutil
import sys

# =============================================================================
# Fill these in...

# https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
GITHUB_TOKEN = '<YOUR GITHUB PERSONAL ACCESS TOKEN HERE>'

# e.g. https://github.com/codePost-college
PARENT_REPO_NAME = 'codePost-college'

DOMAIN = "@school.edu"

# The name of the assignment (regex)
ASSIGNMENT_PATTERN = r"assignment1"

OUTPUT_DIRECTORY = 'codepost_upload'

DEBUG = True

# =============================================================================

headers = {'Authorization': 'token %s' % GITHUB_TOKEN}
url = "https://api.github.com/user/repos?page=1"

_cwd = os.getcwd()
_upload_dir = os.path.join(_cwd, OUTPUT_DIRECTORY)

assignment_regex = re.compile(ASSIGNMENT_PATTERN)

def delete_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)

def add_if_match(candidates, accepted):
    for repo in candidates:
        if assignment_regex.search(repo['name']) and PARENT_REPO_NAME in repo['full_name']:
            accepted.append((repo['name'], repo['clone_url']))

repos = []
response = requests.get(url, headers=headers)
add_if_match(json.loads(response.content), repos)

# Ignore repositories that don't match the ASSIGNMENT_PATTERN
while 'next' in response.links.keys():
    response = requests.get(response.links['next']['url'], headers={"Authorization": 'token %s' % GITHUB_TOKEN})
    add_if_match(json.loads(response.content), repos)

# Overwrite the directories if they exist already
delete_directory(_upload_dir)
os.makedirs(_upload_dir)

for repo in repos:
    username = repo[0].split("-")[-1]
    email = "{}{}".format(username, DOMAIN)

    student_dir = os.path.join(_upload_dir, email)

    cmd = "git clone https://{}@{} {}".format(GITHUB_TOKEN, repo[1].split('//')[1], student_dir)
    if not DEBUG:
        cmd = "{}{}".format(cmd, ">/dev/null 2>&1")
        print('#', end='')
        sys.stdout.flush()

    os.system(cmd)

print()
