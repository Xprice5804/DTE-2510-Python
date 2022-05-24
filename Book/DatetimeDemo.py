from datetime import datetime

# Create a datetime with the specified year, month, and day
d = datetime(2011, 9, 1)
print("timestamp for Sep 1, 2011:", d.timestamp())

# Create a datetime for the current time
d = datetime.now()
print("year:", d.year, "month:", d.month, "day:", d.day,
    "hour:", d.hour, "minute:", d.minute, "second:", d.second)

# Create a datetime with the specified timestamp
d = datetime.fromtimestamp(18000) 
print("year:", d.year, "month:", d.month, "day:", d.day,
    "hour:", d.hour, "minute:", d.minute, "second:", d.second)
