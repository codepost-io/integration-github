import os
import shutil
import argparse
import csv

# =============================================================================

parser = argparse.ArgumentParser(description='GitHub to codePost!')
parser.add_argument(
    'roster', help='The course roster that maps GitHub repo url to student email.')
args = parser.parse_args()

# =============================================================================

# =============================================================================
# Fill these in...

# https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
GITHUB_TOKEN = '<YOUR GITHUB PERSONAL ACCESS TOKEN HERE>'

OUTPUT_DIRECTORY = 'codepost_upload'

_cwd = os.getcwd()
_upload_dir = os.path.join(_cwd, OUTPUT_DIRECTORY)

DEBUG = True

# =============================================================================


def normalize(string):
  return string.lower().strip()


def delete_directory(path):
  if os.path.exists(path):
    shutil.rmtree(path)


def validate_csv(row):
  for key in row.keys():
    if 'clone' in normalize(key):
      repo = key
    elif 'email' in normalize(key):
      email = key

  if repo == None or email == None:
    if repo == None:
      print("Missing header: clone_url")
    if email == None:
      print("Missing header: email")

    raise RuntimeError(
        "Malformatted roster. Please fix the headers and try again.")

    return (repo, email)
  else:
    return (repo, email)


def repo_to_email(roster):
  with open(roster, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    repo, email = (None, None)
    repo_to_email = {}
    for row in csv_reader:
      if line_count == 0:
        (repo, email) = validate_csv(row)
        line_count += 1

      repo_to_email[
          normalize(row[repo])] = normalize(row[email])
      line_count += 1
    return repo_to_email

# =============================================================================

# Overwrite the directories if they exist already
delete_directory(_upload_dir)
os.makedirs(_upload_dir)

repo_to_email = repo_to_email(args.roster)

for repo in repo_to_email:
  email = repo_to_email[repo]
  student_dir = os.path.join(_upload_dir, email)

  cmd = "git clone https://{}@{} {}".format(
      GITHUB_TOKEN, repo.split('//')[1], student_dir)

  if not DEBUG:
    cmd = "{}{}".format(cmd, ">/dev/null 2>&1")
    print('#', end='')
    sys.stdout.flush()

  try:
    os.system(cmd)
  except:
    print("Error: {}".format(repo))

print()
