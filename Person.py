import datetime


class Person:
    def __init__(self, name, birthdate, phonenumber, address):
        """
        Summary line.
        Initializing the variables.
        
        Parameters
        ----------
        name: str
            name of the person
        birthdate: str
            birthdate of the person
            passed as MM/DD/YYYY
        phonenumber: int
            phonenumber of the person
        address: str
            address of the person
            
        Returns
        -------
        Doesn't return anything
        
        """
        self.name = name
        self.birthdate = birthdate
        self.phonenumber = phonenumber
        self.address = address
        
    def getInfo(self):
        """
        Summary line.
        It is an abstract method that returns the info of the person.
        """
        raise NotImplementedError("Subclass must implement abstract method")
        
    def getAge(self):
        """
        Summary line.
        takes birthdate and returns age based off of current datetime
        
        Parameters
        ----------
            
        Returns
        -------
        int
            age of the person
        
        """
        today=datetime.date.today()
        month, day, year = self.birthdate.split("/")
        age = today.year - int(year)
        if (today.month, today.day) < (int(month), int(day)):
            age -=1
        return age
    
