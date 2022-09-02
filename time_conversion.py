#convert seconds to hours, minutes, seconds
import math
input_seconds = int(input("Enter seconds: "))
hours = math.floor(input_seconds / 3600)
minutes = math.floor((input_seconds - (hours * 3600)) / 60)
seconds = input_seconds - (hours * 3600) - (minutes * 60)
print(hours, "jam :", minutes, "menit :", seconds, "detik")