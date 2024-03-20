#Task 1: if-elif-else statements
##This task is designated to convert mass into weight (Newtons)
##and then assess if the weight falls between the parameters of 10 to 1000
mass = float(input("Input object mass in kilograms: "))
weight = mass * 9.8
if weight > 1000:
    print("The object is too heavy: " + str(weight) + "N")
elif weight < 10:
    print("The object is too light: " + str(weight) + "N")
else:
    print("The object weight is within acceptable parameters: " + str(weight) + "N")


#Alt Task 1 with While Loop (Testing variations for having a while loop)
##A variation on Task 1 using While loop so that user can input
##various masses until it reaches acceptable parameters
while True:
    mass = float(input("Input object mass in kilograms: "))
    weight = mass * 9.8   
    if 10 <= weight <= 1000:
        print("The object weight is within acceptable parameters: " + str(weight) + "N")
        break
    elif weight > 1000:
        print("The object is too heavy: " + str(weight) + "N")
    else:
        print("The object is too light: " + str(weight) + "N")

    
    
#Task 2: while loop – input validation
##Checks if an input is outside 1 to 100 and asks for user input
##until number falls within range
num = float(input("Please input a number: "))
while not 1 <= num <= 100:
    print("This number is outside acceptable parameters.")
    num = float(input("Please input a number between 1 to 100: "))
print("Your number is: " + str(num))    


#Task 3: Loops practice
##For loop to sum up total number of bugs counted throughout
##each day for seven days
##includes use of .format() for interface purposes
total_bugs = 0
for day in range(1, 8):
        collected_bug = int(input("Enter the number of bugs collected on day {}:".format(day)))
        while collected_bug < 0:
            print("Please enter a positive number")
            collected_bug = int(input("Reenter the number of bugs collected on day {} as a positive integer:".format(day)))
        total_bugs += collected_bug
print("Total number of bugs collected over seven days: " + str(total_bugs))

