Zybooks Canvas Grader
========
A script to transfer Zybook assignment grades to Canvas.

Remarks
--------
I wrote this while I was working as a student assistant.
Writing this script saved me from having to manually input over a hundred student grades each time a Zybooks assignment was given to the class.

This script automates the entire grading process from logging in to uploading the grades.

A summary of what the script does is as follows:
1. Log in to Zybooks. Then download the grades for the latest assignment as a `.csv`.
2. Log in to Canvas via Microsoft Single Sign-On. Then download the entire gradebook as a `.csv`.
3. Use info from the previous downloads to create a new `.csv` containing grades that can be readily imported into Canvas. Then upload this file to the gradebook.

To automate web interactions (like logging in to a website), I used Python bindings for `Selenium`.<br>
To read and write `.csv` files, I used Python's `csv` module.

Installation
--------
```
git clone <repository_url>
cd zybooks-canvas-grader
py -m pip install --upgrade pip
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Then download a `geckodriver` executable from [this repository](https://github.com/mozilla/geckodriver) and place it in the project's root directory.

Also create a `.env` file in the project's root directory with the following structure:
```
ZYBOOK_EMAIL={zybook_email}
ZYBOOK_PASSWORD={zybook_password}

CANVAS_EMAIL={microsoft_sso_email}
CANVAS_PASSWORD={microsoft_sso_password}

ZYBOOK_IDENTIFIER={zybook_identifier}

CANVAS_SCHOOL_ACRONYM={canvas_school_acronym}
CANVAS_COURSE_IDENTIFIER={canvas_course_identifier}
```

For more information about the `ZYBOOK_IDENTIFIER`, `CANVAS_SCHOOL_ACRONYM` and `CANVAS_COURSE_IDENTIFIER` variables, see the comments in `environment_info.py`.
