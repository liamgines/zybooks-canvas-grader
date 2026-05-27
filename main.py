from zybook import login_and_download_zybook_grades
from canvas import login_and_export_canvas_gradebook, import_grades
from canvas_zybook_grader import create_canvas_grade_report

import os

def delete_files_of_type(extension, directory, ignored_file_names=[]):
    files = os.listdir(directory)
    if extension[0] != ".":
        print("\nNo files deleted.")
        return

    for file_name in files:
        if file_name.endswith(extension) and file_name not in ignored_file_names:
            os.remove(os.path.join(directory, file_name))

def main():
    working_directory = os.getcwd()
    delete_files_of_type(".csv", working_directory, ["import.csv"])

    zybook_assignment_name, zybook_grade_file_name = login_and_download_zybook_grades()
    canvas_gradebook_file_name, driver = login_and_export_canvas_gradebook()

    import_file_name = create_canvas_grade_report(canvas_gradebook_file_name, zybook_grade_file_name, zybook_assignment_name)

    import_file_path = os.path.join(working_directory, import_file_name)
    import_grades(import_file_path, driver)

main()
