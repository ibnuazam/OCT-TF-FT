#convert seconds to days, hours, minutes, seconds
import math
input_seconds = int(input("Enter seconds: "))
days = math.floor(input_seconds / 86400)
hours = math.floor(input_seconds / 3600)
minutes = math.floor((input_seconds - (hours * 3600)) / 60)
seconds = input_seconds - (days * 86400) - (hours * 3600) - (minutes * 60)
print(days, "hari :", hours, "jam :", minutes, "menit :", seconds, "detik")