#LA 5

while True:
    try:
        score = int(input("Enter your grade [0-100]: "))

        grade = score
        if score < 60:
            grade = "F"
        elif score >= 60 and score <= 69:
            grade = "D"

        elif score >= 70 and score <= 79:
            grade = "C"

        elif score >= 80 and score <= 89:
            grade = "B"

        elif score >= 90 and score <= 100:
            grade = "A"
        elif score > 100:
            grade = "A+"
        
        print(f'Score = {score} Grade = {grade}')

    except ValueError:
        print("Invalid Score")