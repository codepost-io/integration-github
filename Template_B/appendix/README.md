# Using a roster to map repositories to students

The example in [Template_B](https://github.com/codepost-io/integration-github/tree/master/Template_B) assumes a standard naming convention for the student repositories.

If the student GitHub repository names are _not_ standardized, then we can generalize the integration by including a `roster.csv` that maps `GitHub Clone URL` to `student email`.

We will walk through that process here.

> Need help? Email us at team@codepost.io

## 0. Setting up the roster

First, create a file `roster.csv` with the following format:

```
clone_url,email
https://github.com/school/assn1-tur.git,turing@school.edu
https://github.com/school/assn1-lis.git,liskov@school.edu
https://github.com/school/assn1-coo.git,cooper@school.edu
```

## 1. Getting your GitHub Personal Access Token

To get a GitHub Personal Access Token, follow [these instructions](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line). Make sure that the token is scoped to 'repos' (see [here](https://cl.ly/a3b1d9af51c2)).

## 2. Setting up the script

Clone this repository or copy the python script `github_to_codepost_template_B_roster.py` to your local machine.

Open the script in a text editor, and update the following variables:

| Variable     | Description                                   |
| ------------ | --------------------------------------------- |
| GITHUB_TOKEN | Your GitHub Personal Access Token from Step 0 |

Copy the `roster.csv` into the same directory.

## 3. Run the script

Make sure that you have Python3 installed and run

`python3 github_to_codepost_template_B_roster.py roster.csv`

After the script terminates, you should see a folder called `codepost_upload` containing the student directories and submissions.

## 4. Upload to codePost

Navigate to [codepost.io](https://codepost.io), log in, and click `Assignments -> Actions -> Upload Submissions -> Multiple Submissions`. Drag `codepost_upload` into codePost and voila.

If you prefer to have more control over the upload process, check out our [Python SDK](https://github.com/codepost-io/codepost-python).

