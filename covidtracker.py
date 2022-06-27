from skrypt import infection_list


class CovidTracker:
    def __init__(self):
        pass

    def getInfectionsForDay(self, month, day):
        for obj in infection_list:
            dataMonth = str(obj.month)
            dataDay = str(obj.date)
            if month == dataMonth and day[0] == dataDay[0] and day[1] == dataDay[1]:
                return obj.number

    def getInfectionsForMonth(self, month):
        listOfInfections = []
        for obj in infection_list:
            dataMonth = str(obj.month)
            if month == dataMonth:
                listOfInfections.append((obj.date, obj.number))
        return listOfInfections

    def getDeathsForDay(self, month, day):
        for obj in infection_list:
            dataMonth = str(obj.month)
            dataDay = str(obj.date)
            if month == dataMonth and day[0] == dataDay[0] and day[1] == dataDay[1]:
                return obj.deaths

    def getDeathsForMonth(self, month):
        listOfInfections = []
        for obj in infection_list:
            dataMonth = str(obj.month)
            if month == dataMonth:
                listOfInfections.append((obj.date, obj.deaths))
        return listOfInfections

    def getHospitalsForDay(self, month, day):
        for obj in infection_list:
            dataMonth = str(obj.month)
            dataDay = str(obj.date)
            if month == dataMonth and day[0] == dataDay[0] and day[1] == dataDay[1]:
                return obj.hospitals
    
    def getHospitalsForMonth(self, month):
        listOfInfections = []
        for obj in infection_list:
            dataMonth = str(obj.month)
            if month == dataMonth:
                listOfInfections.append((obj.date, obj.hospitals))
        return listOfInfections

    def getInfoForDay(self, month, day):
        listOfInfections = []
        for obj in infection_list:
            dataMonth = str(obj.month)
            dataDay = str(obj.date)
            if month == dataMonth and day[0] == dataDay[0] and day[1] == dataDay[1]:
                listOfInfections.append((obj.date, obj.number, obj.deaths, obj.hospitals))
        return listOfInfections
    
    def getInfoForMonth(self, month):
        listOfInfections = []
        for obj in infection_list:
            dataMonth = str(obj.month)
            if month == dataMonth:
                listOfInfections.append((obj.date, obj.number, obj.deaths, obj.hospitals))
        return listOfInfections          
    
    def getInfoForMonths(self):
        listOfInfections = []
        for obj in infection_list:
            listOfInfections.append((obj.date, obj.number, obj.deaths, obj.hospitals))
        return listOfInfections

    def getPercentageIncrease(self):
        listOfInfections = []
        for obj in range(len(infection_list)):
            sumOfWeek = 0
            sumOfEarlierWeek = 0
            for i in range(0,7):
                number = int(infection_list[obj-i].number)
                sumOfWeek += number
            for i in range(7,14):
                number = int(infection_list[obj-i].number)
                sumOfEarlierWeek += number
            PercentageInfections = (((sumOfWeek - sumOfEarlierWeek) / sumOfEarlierWeek) * 100)
            Rounded = float("{:.2f}".format(PercentageInfections)) 
            listOfInfections.append((infection_list[obj].date, Rounded))
        return listOfInfections
    
    def getPercentageWeekWeek(self):
        listOfInfections = []
        for obj in range(len(infection_list)):
            numberx = 0
            numbery = 0
            numberx = int(infection_list[obj].number)
            numbery = int(infection_list[obj-7].number)
            PercentageInfections = (((numberx-numbery)/numbery)*100)
            Rounded = float("{:.2f}".format(PercentageInfections)) 
            listOfInfections.append((infection_list[obj].date, Rounded))
        return listOfInfections
    
