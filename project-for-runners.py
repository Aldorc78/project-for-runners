class Runner:
    maxHeartRate = 0
    def __init__(self, name, gender, weightKg, age, minHeartRate):
        self.name = name
        self.gender = gender
        self.weightKg = weightKg
        self.age = age
        self.minHeartRate = minHeartRate
        
        #This section sets your max heartrate using specific formulas based on your gender
        if self.gender.lower() == "male":
            self.maxHeartRate = 220 - self.age # We use Fox method for males
            print("Your Max HeartRate is: " + str(self.maxHeartRate))
        elif self.gender.lower() == "female": 
            self.maxHeartRate = 206 - (self.age*0.88) # For female we use Gulati
            print("Your Max HeartRate is: " + str(self.maxHeartRate))
        else:
            print("Please select a correct gender, max heartrate stays on 0")
    
aldo = Runner("Aldo", "Male", 78, 23, 46)
