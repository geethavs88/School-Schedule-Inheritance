from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_gets_transportation():
    # Arrange
    name = "Ellis"
    grade = "junior"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)

    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Ansel"
    grade = "senior"
    classes = []

    # Act
    ansel = MiddleSchoolStudent(name, grade, classes)
    
    # Arrange
    assert ansel.name == name
    assert ansel.grade == grade
    assert ansel.classes == []
    # assert len(ansel.classes) == 0

def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Kate"
    grade = "4th grade"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=True)
    expected_summary = (
    '''Kate is a 4th grade enrolled in 1 classes: Painting
    Kate has transportation status'''
    )
    # Assert
    
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert ellis.gets_transportation
    assert ellis.summary() == expected_summary

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Kate"
    grade = "4th grade"
    classes = ["Painting"]

    # Act
    ellis = MiddleSchoolStudent(name, grade, classes, gets_transportation=False)
    expected_summary = (
    "Kate is a 4th grade enrolled in 1 classes: Painting\nKate doesn't have transportation status"
    )
    # Assert
    
    assert ellis.name == name
    assert ellis.grade == grade
    assert ellis.classes == classes
    assert len(ellis.classes) == 1
    assert not ellis.gets_transportation
    assert ellis.summary() == expected_summary