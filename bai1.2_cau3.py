# time
seconds = 42*60 + 42

# miles
miles = 10/1.61

# hours
hours = seconds/3600

# speed
speed = miles/hours

# pace
pace = seconds/miles
minutes = int(pace//60)
sec = pace % 60

print("Seconds:", seconds)
print("Miles:", miles)
print("Speed (mph):", speed)
print("Pace:", minutes, "minutes", sec, "seconds per mile")
