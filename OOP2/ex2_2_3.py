easy = 8*60 + 15      
tempo = 7*60 + 12    
total_time = easy + 3*tempo + easy
start = 6*3600 + 52*60

finish = start + total_time
hours = finish // 3600
minutes = (finish % 3600) // 60

print(f"Về nhà lúc: {hours}:{minutes:02d}")