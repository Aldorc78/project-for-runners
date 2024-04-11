class Runner:
    maxHeartRate = 0
    age = 0
    weightKg = 0    

    def __init__(self, name, gender, weightKg, age, minHeartRate):
        
        self.name = name.lower()
        self.gender = gender.lower()
        self.weightKg = weightKg
       
        if weightKg<=0 or weightKg>200:
            print("Please, select a real weight, your weight is set to: " + str(self.weightKg))
        else:
             self.weightKg = weightKg

        if minHeartRate<=0 or minHeartRate>200:
            print("Please, select a real minimum heart rate, your min heart rate is set to: " + str(self.minHeartRate))
        else:
            self.minHeartRate = minHeartRate


        if age<=0 or age>115:
            print("Please, select a real age, your age is set to: " + str(self.age))
        else:
            self.age = age


        #This section sets your max heartrate using specific formulas based on your gender
        if self.gender == "male":
            self.maxHeartRate = 220 - self.age # We use Fox method for males
            print("Your Max HeartRate is: " + str(self.maxHeartRate))
        elif self.gender == "female": 
            self.maxHeartRate = 206 - (self.age*0.88) # For female we use Gulati
            print("Your Max HeartRate is: " + str(self.maxHeartRate))
        else:
            print("Please select a correct gender, max heartrate stays on 0")
    
aldo = Runner("Aldo", "Male", 78, -2, 46)
