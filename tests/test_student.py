# Wave 1 - Student

from school_schedule.student import Student
def test_student_class_name_is_correct():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  # assert
  assert student.name == "Trenisha"

def test_student_grade_name_is_correct():
  # act
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])
  # assert
  assert student.grade == "senior"

def test_student_classes_is_correct():
  # act 
  student = Student("Trenisha", "senior", ["Calculus", "Choir", "Photography", "AP History"])

  # assert
  assert student.classes == ["Calculus", "Choir", "Photography", "AP History"]  