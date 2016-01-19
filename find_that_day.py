


print("  ________ __                __        ________ __                  __                  __                   ")
print(" /        /  |              /  |      /        /  |                /  |                /  |                  ")
print(" $$$$$$$$/$$/ _______   ____$$ |      $$$$$$$$/$$ |____   ______  _$$ |_           ____$$ | ______  __    __ ")
print(" $$ |__   /  /       \ /    $$ |         $$ |  $$      \ /      \/ $$   |         /    $$ |/      \/  |  /  |")
print(" $$    |  $$ $$$$$$$  /$$$$$$$ |         $$ |  $$$$$$$  |$$$$$$  $$$$$$/         /$$$$$$$ |$$$$$$  $$ |  $$ |")
print(" $$$$$/   $$ $$ |  $$ $$ |  $$ |         $$ |  $$ |  $$ |/    $$ | $$ | __       $$ |  $$ |/    $$ $$ |  $$ |")
print(" $$ |     $$ $$ |  $$ $$ \__$$ |         $$ |  $$ |  $$ /$$$$$$$ | $$ |/  |      $$ \__$$ /$$$$$$$ $$ \__$$ |")
print(" $$ |     $$ $$ |  $$ $$    $$ |         $$ |  $$ |  $$ $$    $$ | $$  $$/       $$    $$ $$    $$ $$    $$ |")
print(" $$/      $$/$$/   $$/ $$$$$$$/          $$/   $$/   $$/ $$$$$$$/   $$$$/         $$$$$$$/ $$$$$$$/ $$$$$$$ |")
print("                                                                                                   /  \__$$ |")
print("                                                                                                   $$    $$/ ")
print("                                                                                                    $$$$$$/  ")



#vivliothiki gia thn sunarthsh math.floor pou xreiazetai ston typo tou Gauss
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

#elegxos egkurothtas hmeromhnias
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

#tropopoihsh metavlhtwn vasei ths thewrias tou Gauss
if (month==1):
    month=1
    y=(year%100)-1
elif (month==2):
    month=12
    y=(year%100)-1

else:
    month=month-2
    y=year%100
c=(year//100)
d=day

#typos tou Gauss
w=(d+math.floor(2.6*month-0.2)+y+math.floor(y/4)+math.floor(c/4)-2*c)%7

if  (w==0 and error==0):
    print("Sunday")
elif(w==1 and error==0):
    print("Monday")
elif(w==2 and error==0):
    print("Tuesday")
elif(w==3 and error==0):
    print("Wednesday")
elif(w==4 and error==0):
    print("Thursday")
elif(w==5 and error==0):
    print("Friday")
elif(w==6 and error==0):
    print("Saturday")
