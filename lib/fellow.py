""" 
  Fellow resides here

"""
from .person import Person

class Fellow(Person):
    def __init__(self, name, amity_interest = "N", amity_room_name = None):
        super(Fellow, self).__init__(name)
        self.amity_interest = amity_interest
        self.amity_room_name = amity_room_name

    def set_amity_interest(self, amity_interest):
        self.amity_interest = amity_interest

    def set_amity_room_name(self, amity_room_name):
        self.amity_room_name = amity_room_name

    def show_fellow_info(self):
        print("Name: %s" % (self.name))
        print("Office: %s" % (self.office_name))
        print("Amity Room: %s" % (self.amity_room_name))