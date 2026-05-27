import csv

def create_canvas_grade_report(canvas_gradebook_file_name, zybook_grade_file_name, assignment_name):
    import_file_name = "import.csv"
    points_to_earn = "100"

    assert assignment_name != "" and import_file_name != "" and points_to_earn != ""

    canvas_student_column_count = 4
    zybook_student_column_count = 8 + 1 + 1

    with open(canvas_gradebook_file_name, "r") as canvas_gradebook:
        canvas_reader = csv.reader(canvas_gradebook)

        first_canvas_row = next(canvas_reader)

        canvas_student_column = first_canvas_row.index("Student", 0, canvas_student_column_count)
        canvas_id_column = first_canvas_row.index("ID", 0, canvas_student_column_count)
        canvas_sis_login_column = first_canvas_row.index("SIS Login ID", 0, canvas_student_column_count)
        canvas_section_column = first_canvas_row.index("Section", 0, canvas_student_column_count)

        second_canvas_row = next(canvas_reader)

        assert second_canvas_row[canvas_student_column] == "    Points Possible"
        assert second_canvas_row[canvas_id_column] == second_canvas_row[canvas_sis_login_column] == second_canvas_row[canvas_section_column] == ""
        
        student_grades = {}
        canvas_student_count = 0
        for row in canvas_reader:
            student_id_number = row[canvas_sis_login_column]

            """Initializing all grades as NULL"""
            student_grades[student_id_number] = ""

            canvas_student_count += 1

        assert canvas_student_count == len(student_grades)

        with open(zybook_grade_file_name, "r") as zybook_assignment_grades:
            zybook_reader = csv.reader(zybook_assignment_grades)
            
            first_zybook_row = next(zybook_reader)

            zybook_student_id_column = first_zybook_row.index("Student ID", 0, zybook_student_column_count)
            try:
                zybook_percent_grade_column = first_zybook_row.index("Percent grade", 0, zybook_student_column_count)

            except:
                zybook_percent_grade_column = first_zybook_row.index("Percent score", 0, zybook_student_column_count)

            invalid_zybook_students = []
            for row in zybook_reader:
                student_id_number = row[zybook_student_id_column]
                assignment_grade = row[zybook_percent_grade_column]

                assert assignment_grade != ""

                float(assignment_grade)

                try:
                    if student_grades[student_id_number] != "":
                        raise LookupError

                    student_grades[student_id_number] += assignment_grade

                except:
                    invalid_zybook_students.append(student_id_number)

                    """
                    Below is sample code to handle when students incorrectly input their Student ID into Zybooks.

                    if student_id_number == "invalid_id":
                        StudentName = "valid_id"
                        assert student_grades[StudentName] == ""
                        student_grades[StudentName] += assignment_grade

                    
                    elif student_id_number == "another_invalid_id":
                    """

            print()
            if len(invalid_zybook_students) != len(set(invalid_zybook_students)):
                print(f"WARNING: Zybook Student IDs have repeats: {invalid_zybook_students}\n\nNo grade was updated.\n")
                raise ValueError

            print(f"Invalid Zybook Student IDs found: {invalid_zybook_students}")

        new_canvas_assignment_rows = []

        new_canvas_assignment_rows.append(first_canvas_row[0 : canvas_student_column_count])
        new_canvas_assignment_rows[0].append(assignment_name)

        assert len(new_canvas_assignment_rows[0]) == canvas_student_column_count + 1

        new_canvas_assignment_rows.append(second_canvas_row[0 : canvas_student_column_count])
        new_canvas_assignment_rows[1].append(points_to_earn)

        assert len(new_canvas_assignment_rows[1]) == canvas_student_column_count + 1

        canvas_gradebook.seek(0)
        next(canvas_reader)
        next(canvas_reader)

        for row in canvas_reader:
            student_id_number = row[canvas_sis_login_column]
            assignment_grade = student_grades[student_id_number]

            new_canvas_assignment_rows.append(row[0 : canvas_student_column_count])
            if assignment_grade == "":
                new_canvas_assignment_rows[-1].append(assignment_grade)
            else:
                new_canvas_assignment_rows[-1].append(str(float(assignment_grade) / float(100) * float(points_to_earn)))

            assert len(new_canvas_assignment_rows[-1]) == canvas_student_column_count + 1


    assert len(new_canvas_assignment_rows) == canvas_student_count + 2

    with open(import_file_name, "w") as updated_canvas_grades:
        updated_canvas_grades_writer = csv.writer(updated_canvas_grades, delimiter=",", quoting=csv.QUOTE_MINIMAL, lineterminator="\n")

        for row in new_canvas_assignment_rows:
            updated_canvas_grades_writer.writerow(row)

    return import_file_name
