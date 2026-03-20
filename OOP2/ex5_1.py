import time
current_time = time.time()

days = int(current_time / (24*3600))
remaining_seconds = current_time % (24*3600)
hours = int(remaining_seconds / 3600)
remaining_seconds %= 3600
minutes = int(remaining_seconds / 60)
seconds = int(remaining_seconds % 60)




print("Days since epoch:", days)
print("Current time:", hours, ":", minutes, ":", seconds)