#TEMPERATURE CHECKER 
#LA3

temp = int(input("Enter The Current temperature: "))
if temp <0:
print("ITS FREEZING COLD!")   
elif temp >= 0 and temp <= 10:
print("Cold day isnt it?") 
elif temp <= 30:
print("Pleasant Weather! Nice day for fishing innit?")
elif temp > 30:
print("Hot day isnt it? Stay Hydrated!")   
