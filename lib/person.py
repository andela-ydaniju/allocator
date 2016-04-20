"""
  This class is where the model for every Andelan - fellow of staff resides

"""
class Person(object):
    def __init__(self, name, office_name = None):
        self.name = name
        self.office_name = office_name

    def assign_office(self, office_name):
        self.office_name = office_name
