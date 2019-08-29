# =============================================================================
# codePost – GitHub Classroom Utility
#
# Takes submissions downloaded from Github Classroom and transforms the file
# structure into a structure that codePost will recognize.
#
# =============================================================================

# Python stdlib imports
import os
import argparse
import csv
import shutil
from distutils.dir_util import copy_tree

# =============================================================================

parser = argparse.ArgumentParser(description='GitHub Classroom to codePost!')
parser.add_argument(
    'submissions', help='The directory of submissions downloaded from GitHub Classroom')
parser.add_argument(
    'roster', help='The course roster of students that includes github_username and codePost email')
args = parser.parse_args()

# =============================================================================
# Constants

OUTPUT_DIRECTORY = 'codepost_upload'

_cwd = os.getcwd()
_upload_dir = os.path.join(_cwd, OUTPUT_DIRECTORY)

DEBUG = True

# =============================================================================
# Helpers


def normalize(string):
  return string.lower().strip()


def delete_directory(path):
  if os.path.exists(path):
    shutil.rmtree(path)


def validate_csv(row):
  for key in row.keys():
    if 'github_username' in normalize(key):
      github_username = key
    elif 'codepost_email' in normalize(key):
      codepost_email = key

  if github_username == None or codepost_email == None:
    if github_username == None:
      print("Missing header: github_username")
    if codepost_email == None:
      print("Missing header: codepost_email")

    raise RuntimeError(
        "Malformatted roster. Please fix the headers and try again.")

    return (github_username, codepost_email)
  else:
    return (github_username, codepost_email)


def name_to_email(roster):
  with open(roster, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    github_username, codepost_email = (None, None)
    name_to_email = {}
    for row in csv_reader:
      if line_count == 0:
        (github_username, codepost_email) = validate_csv(row)
        line_count += 1

      # Map {GitHub username} to {codePost email}
      name_to_email[row[github_username]] = normalize(row[codepost_email])
      line_count += 1
    return name_to_email

# =============================================================================

if DEBUG:
  print('\nSetting up directories...')

# Overwrite the directories if they exist already
delete_directory(_upload_dir)
os.makedirs(_upload_dir)

if DEBUG:
  print('\t/{}'.format(OUTPUT_DIRECTORY))

if DEBUG:
  print('\nReading and validating roster...')

name_to_email = name_to_email(args.roster)
if DEBUG:
  print('\tVALID')

if DEBUG:
  print('\nCopying folders...')

files = os.listdir(args.submissions)
folders = []

for f in os.listdir(args.submissions):
  from_directory = os.path.join(args.submissions, f)
  if os.path.isdir(from_directory):
    if f in name_to_email:
      to_directory = os.path.join(_upload_dir,name_to_email[f])
      copy_tree(from_directory, to_directory)
      if DEBUG:
        print('\t{}'.format(name_to_email[f]))

