import datetime
import datetime

today = datetime.datetime.today()
print(f"Today : {today}")

birthday = datetime.date(1999, 10, 7)
print(f"Birthday : {birthday}")

birthday = datetime.datetime(1999, 10, 7)
print(f"Birthday : {birthday}")

days_since_birth = (today - birthday)
print(days_since_birth)

tdelta = datetime.timedelta(days = 1)
print(today - tdelta)

print(datetime.time(7, 25, 53))

# datetime.date (Y, M, D)
# datetime.time (h, m, s, ms)
# datetime.datetime (Y, M, D, h, m, s, ms)

hours_delta = datetime.timedelta(hours = 24)
print(today + hours_delta)


import pytz
UTC_datetime_today = datetime.datetime.now(tz = pytz.UTC)
print(f"UTC datetime today : {UTC_datetime_today}")
IST_datetime_today = datetime.datetime.now(tz = pytz.timezone('Asia/Kolkata'))
print(f"IST datetime today : {IST_datetime_today}")


''' 2022-06-30 -> June 30, 2022 by using strftime, where f = formatting '''
print(IST_datetime_today.strftime("%B %d, %Y")) # %B -> Month, %d -> day, %Y -> Year

''' June 30, 2022 -> 2022-06-30 by using strptime, where p = parsing '''
print(datetime.datetime.strptime("June 30, 2022", "%B %d, %Y"))
