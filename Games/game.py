'Purpose: Determine and display letter grades.'
"Students: Marvin Santos, Minkee, Max"

grade = int(input("What is your grade percent? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Your letter grade is: {letter}")

if grade >= 70:
    print("Congratulations! You passed the class!")
else:
    print("Stay focused and you'll get it next time!")

