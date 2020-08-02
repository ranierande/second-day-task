#program to get the last day of a specified year and month
import calendar
year=2018
month=3
print(calendar.monthrange(year,month)[1])
