grade = int(input("Enter your marks (0-100): "))

if grade >= 90:
    print("You got an A!")
elif grade >= 80:
    print("You got a B!")
elif grade >= 70:
    print("You got a C!")
elif grade >= 60:
    print("You got a D!")
elif grade >= 40:
    print("You got an E!")
else:
    print("You got an F!")