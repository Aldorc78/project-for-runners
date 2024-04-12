class Runner:
    maxHeartRate = 0
    age = 0
    weightKg = 0 

    aerobicZones = {"zone1": [], "zone2": [],"zone3": [], "zone4": [], "zone5": []}

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
        
        #This for section is going to calculate the aerobic zones of the runner
        #each zone is a range so they have two limits 
        lLimitZone1 = (50*self.maxHeartRate)/100 
        uLimitZone1 = (60*self.maxHeartRate)/100 

        lLimitZone2 = (61*self.maxHeartRate)/100 
        uLimitZone2 = (70*self.maxHeartRate)/100 

        lLimitZone3 = (71*self.maxHeartRate)/100 
        uLimitZone3 = (80*self.maxHeartRate)/100    

        lLimitZone4 = (81*self.maxHeartRate)/100 
        uLimitZone4 = (90*self.maxHeartRate)/100      

        lLimitZone5 = (91*self.maxHeartRate)/100 
        uLimitZone5 = (100*self.maxHeartRate)/100    

        #i = 1
        #for zone in self.aerobicZones:
          #  self.aerobicZones["zone{}".format(i)].append(lLimitZone1)
           # self.aerobicZones["zone{}".format(i)].append(uLimitZone1) 
            


        self.aerobicZones["zone1"].append(lLimitZone1) 
        self.aerobicZones["zone1"].append(uLimitZone1) 
        self.aerobicZones["zone2"].append(lLimitZone2) 
        self.aerobicZones["zone2"].append(uLimitZone2)         
        self.aerobicZones["zone3"].append(lLimitZone3) 
        self.aerobicZones["zone3"].append(uLimitZone3)            
        self.aerobicZones["zone4"].append(lLimitZone4) 
        self.aerobicZones["zone4"].append(uLimitZone4)      
        self.aerobicZones["zone5"].append(lLimitZone5) 
        self.aerobicZones["zone5"].append(uLimitZone5)            
      



aldo = Runner("Aldo", "Male", 78, 23, 46)

print(aldo.aerobicZones)