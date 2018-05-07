class Person:
    def __init__(self,initialAge):
        """ Creating our intitial variable and
            checking against negatives.
        """
        self.initialAge = initialAge
        if self.initialAge < 0:
            self.initialAge = 0
            print("Age is not valid, setting age to 0.")
    
    def amIOld(self):
        """ printing our statements to meet
            test criteria.
        """
        if self.initialAge < 13:
            print("You are young.")
        elif self.initialAge >= 13 and self.initialAge < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
            
    def yearPasses(self):
        """ Adding a year for test criteria. """
        self.initialAge += 1  
