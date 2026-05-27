import os
from dotenv import load_dotenv

load_dotenv()

zybook_email = os.environ["ZYBOOK_EMAIL"]
zybook_password = os.environ["ZYBOOK_PASSWORD"]

canvas_email = os.environ["CANVAS_EMAIL"]
canvas_password = os.environ["CANVAS_PASSWORD"]

"""
Zybook Identifier Format:

    School
    Department
    Course Number
    Instructor
    Semester
    Year

This can be found at the end of your Zybook's designated URL (learn.zybooks.com/zybook/ZYBOOK_IDENTIFIER).
"""
zybook_identifier = os.environ["ZYBOOK_IDENTIFIER"]

"""
The canvas school acronym variable will often be the colloquial name of your school.

This can be found at the start of your school's Canvas URL (CANVAS_SCHOOL_ACRONYM.instructure.com).
"""
canvas_school_acronym = os.environ["CANVAS_SCHOOL_ACRONYM"].lower()

"""
Canvas Course Identifier Format: #####

This can be found at the end of your Canvas course's designated URL (https://CANVAS_SCHOOL_ACRONYM.instructure.com/courses/CANVAS_COURSE_IDENTIFIER).
"""
canvas_course_identifier = os.environ["CANVAS_COURSE_IDENTIFIER"]
