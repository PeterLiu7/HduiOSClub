def years(n):
    if((n % 4 == 0 and n % 100 != 0) or n % 400 == 0):
        return 1
    else:
        return 0
def panduan(year,month,day):
    daynum=0
    monthnum=1
    months=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (years(year)== 1):
        months=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in months:
        if(monthnum<month):
            daynum+=i
            monthnum+=1
    daynum+=day
    print (daynum)

panduan(2017,11,1)