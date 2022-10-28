#quiz game that prints user score, percentage and quiz remarks

score = 0

print("Welcome to MY WORLD GAME!")
numb1 = input("What continent is Nigeria located? ").lower()
if numb1 == "africa":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!")

numb2 = input("What continent is Italy located? ").lower()
if numb2 == "europe":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!")

numb3 = input("What continent is China located? ").lower()
if numb3 == "asia":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!")

numb4 = input("What continent is New Zealand located? ").lower()
if numb4 == "australia":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!")

numb5 = input("What continent is Morrocco located? ").lower()
if numb5 == "africa":
    print("Correct!")
    score += 1
else:
    print("INCORRECT!")

print("You got " + str(score) + " questions correct!")
percentage = (score/5) * 100
print("You got " + str((score/5) * 100) + "%")

if percentage < 20:
    print("Try Harder!")
elif percentage < 50:
    print("You can do better")
elif percentage < 70:
    print("Yes! You did it!")
else:
    print("You're a scholar!")

