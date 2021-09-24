from school_schedule.student import Student

# Wave 2 -- test add_class function 

# make sure the class added is actually now in the classes list
def test_add_class_adds_to_class_list():
    # arrange
    rhyannon = Student("Rhyannon", "freshman", ["pottery", "drama", "gender trouble"])
    course = "programming!!!"

    # act
    rhyannon.add_class(course)

    # assert 
    assert "programming!!!" in rhyannon.classes 
    assert len(rhyannon.classes) == 4 
    


# make sure list is one longer than it was before 