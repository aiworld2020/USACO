"""
ID: aryanra2
LANG: PYTHON3
TASK: friday
"""

n = 0
num_of_13ths = [0, 0, 0, 0, 0, 0, 0]
days_per_year = 0
days_per_month = 31
year = 1900
splitted = []


f = open("friday.in", mode = "r")
content = f.read()
splitted = content.split("\n")
    
def getN():
    n = splitted[0]
    return int(n)

def daysPerYear(year):
    if year % 100 == 0:
        if year % 400 == 0:
            days_per_year = 366
            return days_per_year
        else:
            days_per_year = 365
            return days_per_year
    elif year % 4 == 0:
        days_per_year = 366
        return days_per_year
    else:
        days_per_year = 365
        return days_per_year

def checkMonth(month, days_per_year):
    if month == 4 or month == 6 or month == 9 or month == 11:
        days_per_month = 30
    elif month == 2:
        if days_per_year == 366:
            days_per_month = 29
        else:
            days_per_month = 28
    else:
        days_per_month = 31
    return days_per_month

def check13ths():
    month = 1
    date = 1
    day_of_the_week = 2
    end_year = year
    #print("num of years", n)
    while end_year <= year + n - 1:
        #print("inside first loop")
        days_per_year = daysPerYear(end_year)
        #print("Days in year =", end_yeardays_per_year )
        days_per_month = checkMonth(month, days_per_year)
        #print("dpm", days_per_month)
        #print("month =", month)
        while True:
            #print("here")
            if day_of_the_week == 7:
                #if month == 1 or month == 2:
                    # print("year", end_year)
                    # print("month", month)
                    # print("date", date)
                    # print("dotw", day_of_the_week)
                day_of_the_week = 0
                
            if date == 13:
                num_of_13ths[day_of_the_week] += 1
            
             #print("**date ",date)
            if date == days_per_month:
                date = 0
                month += 1
                break
            
            
            date += 1
            day_of_the_week += 1
            
            
                
        if month == 13:
            date = 0
            month = 1
            end_year += 1
            #print("end_year = ", end_year)
            
def outputFile():
    with open("friday.out", mode = "w") as f:
        for i in range(0, len(num_of_13ths)):
            if i == len(num_of_13ths) - 1:
                f.write(str(num_of_13ths[i]))
            else:
                f.write(str(num_of_13ths[i]) + " ")
        f.write("\n")

n = getN()
check13ths()
#print(num_of_13ths)
outputFile()


