import datetime

class Person:
    """ Abstract person class for defining similarity between both employees and customers """
    def __init__(self, name, birthdate, phone, address):
        self.name = name
        self.__birthdate = birthdate
        self.__phone = phone
        self.__address = address
        
    def getInfo(self):
        """
        abstract method that returns the info of the person

        """
        raise NotImplementedError("Subclass must implement abstract method")
        
    def getAge(self):
        """
        takes birthdate and returns age based off of current datetime

        """
        today=datetime.date.today()
        month, day, year = self.__birthdate.split("/")
        age = today.year - int(year)
        if (today.month, today.day) < (int(month), int(day)):
            age -=1

        return age
