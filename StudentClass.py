import datetime

class Student:
    def __init__(self, student_id, name, dob, classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__classification = classification
    
    
    def calc_current_age(self):
        dob_parts = self.__dob.split('/')
        dob_month = int(dob_parts[0])
        dob_day = int(dob_parts[1])
        dob_year = int(dob_parts[2])

        current_year = datetime.datetime.now().year

        age = current_year - dob_year

        return age
    

    def get_registration_date(self):
        if self.__classification == "Sr":
            return "4/1 through 4/3"
        elif self.__classification == "Jr":
            return "4/4 through 4/6"
        elif self.__classification == "So":
            return "4/7 through 4/9"
        elif self.__classification == "Fr":
            return "4/10 through 4/12"
        else:
            return "Invalid classification" 