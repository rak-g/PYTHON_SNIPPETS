# GRADE CRITERIA
# Scores 91 - 100 : Grade = "Outstanding"
# Scores 81 - 90 : Grade = "Exceeds Expectations"
# Scores 71 - 80 : Grade = "Acceptable"
# Scores < 70 : Grade = "Fail"

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

print("STUDENT SCORES")
print(student_scores)

student_grades = {}

for student in student_scores:
    score_value = student_scores[student]
    if score_value > 90:
        student_grades[student] = "Outstanding"
    elif score_value > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score_value > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print("STUDENT GRADES")
print(student_grades)
