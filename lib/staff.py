from .person import Person

class Staff(Person):
    def __init__(self, name):
        super(Staff, self).__init__(name)

    def show_staff_info(self):
        print("Name: %s" % (self.name))
        print("Office: %s" % (self.office_name))