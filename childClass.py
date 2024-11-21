class sleepHabits(Giraffe):
    def __init__(self, age, sleepHours):
        super().__init__(age, sleepHours)
        self.age = 5
        self.sleepHours = 4
        
        return self.age * self.sleepHours
        
