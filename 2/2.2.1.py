import datetime

year, month, day = [int(i) for i in input().split(" ")]
days = int(input())

current = datetime.date(year,month,day)
delta = datetime.timedelta(days)
print((current + delta).strftime('%Y %-m %-d'))