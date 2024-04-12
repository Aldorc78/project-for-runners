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

        zonesPercentages =[(50,60), (61,70), (71,80), (81,90), (91,100)]  

        
        for zone in zonesPercentages:

            lLimit = (zone[0]*self.maxHeartRate)/100
            uLimit = (zone[1]*self.maxHeartRate)/100

            i = zonesPercentages.index(zone) + 1 

            self.addAerobicZone(f'zone{i}',lLimit, uLimit)
        

    def addAerobicZone(self,zone, minH, maxH):
        self.aerobicZones[zone].append(minH)
        self.aerobicZones[zone].append(maxH)





aldo = Runner("Aldo", "Male", 78, 23, 46)

print(aldo.aerobicZones)
#print(globals())
#print(locals())