# Importing submissions into codePost from GitHub 
### _Course Template A – Student Repositories_

In Course Template A, every student has a single repository for the course. Each assignment is a new directory within the repository.

Here is a visual example:

```
course_admin/
  cs1-turing/
    Assignment1/
    Assignment2/
  cs1-liskov/
    Assignment1/
    Assignment2/
  cs1-cooper/
    Assignment1/
    Assignment2/
```

> Make sure that the name of each student repository is the same as their email prefix. Example: `/turing` -> turing@school.edu

Running the `github_to_codepost_template_A` script will create a folder called `codepost_upload` which you can drag-and-drop into codePost to upload the submissions.

The process will only take a few minutes, start to finish.

> Need help? Email us at team@codepost.io

## 0. Getting your GitHub Personal Access Token

To get a GitHub Personal Access Token, follow [these instructions](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). Make sure that the token is scoped to 'repos' (see [here](https://cl.ly/a3b1d9af51c2)).

## 1. Setting up the script

Clone this repository or copy the python script `github_to_codepost_template_A.py` to your local machine.

Open the script in a text editor, and update the following variables:

| Variable           | Description                                                                                                                               |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| GITHUB_TOKEN       | Your GitHub Personal Access Token from Step 0                                                                                             |
| PARENT_REPO_NAME   | The name of the user or organization that created the repositories (`course_admin` in the example above)                                  |
| DOMAIN             | The email domain to append to usernames. A domain of `@school.edu` will map `turing` to `turing@school.edu`.                              |
| COURSE_PATTERN     | The regular expression that will match relevant student repositories. `cs1` in the example above.                                         |
| ASSIGNMENT_PATTERN | The regular expression that will match the current assignment folders. `Assignment1` in the example above to get Assignment1 submissions. |

## 3. Run the script

Make sure that you have Python3 installed and run

`python3 github_to_codepost_template_A.py`

After the script terminates, you should see a folder called `codepost_upload` containing the student directories and submissions.

## 4. Upload to codePost

Navigate to [codepost.io](https://codepost.io), log in, and click `Assignments -> Actions -> Upload Submissions -> Multiple Submissions`. Drag `codepost_upload` into codePost and voila.

If you prefer to have more control over the upload process, check out our [Python SDK](https://github.com/codepost-io/codepost-python).
