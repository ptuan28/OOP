time_seconds = 42*60 + 42
miles = 10 / 1.61

pace= time_seconds / miles

minutes = int(pace / 60)
seconds = int(pace % 60)
speed = miles / (time_seconds / 3600)

print("toc do trung binh tính bằng phút tren dam:" ,minutes)
print("toc do trung binh tính bằng giay tren dam:" ,seconds)
print("van toc trung binh tính bằng dam tren gio:" ,speed)
