# Importing submissions into codePost from GitHub Classroom

We will use the [GitHub Classrooom Assistant](https://classroom.github.com/assistant) to download assignment submissions to our local machine in a file structure that codePost will recognize.

The process will only take a minute, start to finish.

> Need help? Email us at team@codepost.io

## 0. Setting up the roster

First, download the course roster from GitHub Classroom. It will be in the following format:

```
identifier,github_username,github_id,name
turing@gmail.com,turing,10101,Alan Turing
liskov@gmail.com,liskov,20202,Barbara Liskov
cooper@gmail.com,cooper,30303,Sheldon Cooper
```

Next, add a new column with the corresponding codePost email (in some cases, this will be the same as the GitHub identifier):

```
identifier,github_username,github_id,name,codepost_email
turing@gmail.com,turing,10101,Alan Turing,turing@school.edu
liskov@gmail.com,liskov,20202,Barbara Liskov,liskov@school.edu
cooper@gmail.com,cooper,30303,Sheldon Cooper,cooper@school.edu
```

## 1. Download submissions

Install the [GitHub Classrooom Assistant](https://classroom.github.com/assistant) and download the submissions for this assignment.

## 2. Setting up the script

Clone this repository or copy the python script `github_to_codepost_github_classroom.py` to your local machine.

Make sure that the script, the downloaded submissions folder, and the updated `classroom_roster.csv` are in the same directory.

## 3. Run the script

Make sure that you have Python3 installed and run

`python3 github_to_codepost_github_classroom.py downloaded_submissions classroom_roster.csv`

After the script terminates, you should see a folder called `codepost_upload` containing the student directories and submissions.

## 4. Upload to codePost

Navigate to [codepost.io](https://codepost.io), log in, and click `Assignments -> Actions -> Upload Submissions -> Multiple Submissions`. Drag `codepost_upload` into codePost and voila.

If you prefer to have more control over the upload process, check out our [Python SDK](https://github.com/codepost-io/codepost-python).
