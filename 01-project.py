
#mini bank command prompt project that collects input from the user and displays various options

#methods used: if statements and string concatenation


name = input("What is your name? ")
print("Hello " + name)
print("How can I help you? " + name)
action = input("Please press 1 for account assistance and 0 to speak to a representative. ")
if action == "1":
    print("You are now being redirected for account assistance ")
elif action == "0":
    print("You are being transferred to a call center agent ")
else:
    print("Invalid Input")
