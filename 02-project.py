#function definition 

#script to analyse weather temperature and output information based on current temperature range


def weather(temp, locatn):
    print("It is ", temp, "in ", locatn, "today is a good day!")
    return weather

location = input("Enter your current location ")
temperature = int(input("Enter temperature "))

prompt = weather(temperature, location)
print(prompt)
