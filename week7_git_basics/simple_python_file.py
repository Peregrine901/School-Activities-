    try:
        temp = int(input("Enter The Current temperature: "))
        
        if temp < 0:
            print("ITS FREEZING COLD!")
        elif temp <= 10:
            print("Cold day isn't it?")
        elif temp <= 30:
            print("Pleasant Weather! Nice day for fishing innit?")
        else:
            print("Hot day isn't it? Stay Hydrated!")
        
        cont = input("Do you want to continue? [YES/NO]: ").strip().lower()
        if cont in ["no", "n"]:
            print("Goodbye!")
            break

    except ValueError:
        print("Invalid Input! Try again")
