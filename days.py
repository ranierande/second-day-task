#program to print next 5 days starting from taoday
import datetime
base=datetime.datetime.today()
for x in range(0,5):
    print(base+datetime.timedelta(days=x))
