""" check input year is leap year or not """

year=int(input("Enter year to be checked:"))

if(year%4==0 and year%100!=0 or year%400==0):
    print("The year {0} is a leap year!".format(year))
else:
    print("The year {0} isn't a leap year!".format(year))