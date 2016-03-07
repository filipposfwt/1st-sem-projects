print(" ______ _           _   _______ _           _         _")
print(" |  ____(_)         | | |__   __| |         | |       | |")
print(" | |__   _ _ __   __| |    | |  | |__   __ _| |_    __| | __ _ _   _")
print(" |  __| | | '_ \ / _` |    | |  | '_ \ / _` | __|  / _` |/ _` | | | |")
print(" | |    | | | | | (_| |    | |  | | | | (_| | |_  | (_| | (_| | |_| |")
print(" |_|    |_|_| |_|\__,_|    |_|  |_| |_|\__,_|\__|  \__,_|\__,_|\__, |")
print("                                                                __/ |")
print("                                                               |___/ ")
#Math library that is needed in the Gauss formula
import math

print ("Give date in the form of dd/mm/yyyy(ex.12/2/2008)")
print("")
date=raw_input("Date:")
print("")
date=date.split("/")
day=int(date[0])
month=int(date[1])
year=int(date[2])
error=0

#Checking date's validity
if (day<1 or month<1):
    print("Seriously now? Please enter positive data.")
    error=1
elif (year<1):
    print("Well ,write your own code for BC dates!!!")
    error=1
elif (month>12):
    print("Come on,there are only 12 months,this is A grade stuff!")
    error=1
elif (month==2):
    if(day>28 and year%4!=0):
        print("Invalid date for February in a non leap year ,last day is the 28th!")
        error=1
    elif(day>29 and year%4==0):
        print("Invalid date for February in a leap year ,last day is the 29th!")
        error=1
elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    if (day>31):
        print("There are 31 days in this month you fool!")
        error=1
elif(month==4 or month==6 or month==9 or month==11):
    if (day>30):
        print("There are 30 days in this month you fool!")
        error=1

#Adjusting variables according to Gauss theory
if (month==1):
    month=11
    y=(year%100)-1
elif (month==2):
    month=12
    y=(year%100)-1
else:
    month=month-2
    y=year%100
c=(year//100)
d=day

#Gauss formula
w=(d+math.floor(2.6*month-0.2)+y+math.floor(y/4)+math.floor(c/4)-2*c)%7
if (error==0):
    if  (w==0):
        print("Sunday")
    elif(w==1):
        print("Monday")
    elif(w==2):
        print("Tuesday")
    elif(w==3):
        print("Wednesday")
    elif(w==4):
        print("Thursday")
    elif(w==5):
        print("Friday")
    elif(w==6):
        print("Saturday")
