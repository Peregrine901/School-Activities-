#LA 4 
age = int(input("Enter your age: "))
val_id = input("do you have a valid i'd? [yes/no]")

has_valid_id = (val_id == "yes")          
is_adult = (age >= 18)                    
is_senior = (age >= 60)                   

eligibility = has_valid_id and is_adult      
senior_discount = eligibility and is_senior  

if eligibility == True:
    print("Eligable")
elif senior_discount == True:
    print("Eligible")
else:
    print("you are not eligable")