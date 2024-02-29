# Dictionary of student names and their respective scores
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Initialize an empty dictionary to store student grades
student_grades = {}

# Iterate through each student in the student_scores dictionary
for key in student_scores:
  # Check the score and assign a grade based on the score
  if student_scores[key] >= 90:
    student_grades[key] = 'Outstanding'  # 90 and above
  elif student_scores[key] >= 80:
    student_grades[key] = 'Exceeds Expectations'  # 80 to 89
  elif student_scores[key] >= 70:
    student_grades[key] = 'Acceptable'  # 70 to 79
  else:
    student_grades[key] = 'Fail'  # Below 70

# Print the final dictionary of student grades
print(student_grades)
