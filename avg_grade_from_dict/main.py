# Example starting point:
students_grades = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92
}


def find_avg_grade(grade_dict):
    grade_total = 0
    for grade in grade_dict.values():
        grade_total += grade
    return grade_total / len(grade_dict)
