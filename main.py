#Main program:
choice=0 #declaring the variable and initializing it with 0 value
cat=0 #declaring the variable and initializing it with 0 value
print("\n\t\t* BMI CALCULATOR *")
#Reading the details of the user
name=input("Enter your NAME : ")
gender=input("Enter your GENDER : \n\n * Male \t * Female \t * Others \n\n")
#clear_output(wait=True)
age=input("Enter your AGE in years : ")
weight = input("Enter your WEIGHT in KGS :")
height = input("Enter your HEIGHT in CMS:")
#clear_output(wait=True)
otp=random.randint(1111,9999) #generating a random 4- digit number as an otp
print("\nWe have generated an OTP for you to access the calculator:\nYOUR OTP IS ",otp)
while True: #checking the otp until the user enters it correct
    check=int(input("\nPlease Enter the shown OTP to access the calculator : "))
    if check==otp: #checking if the entered otp was same or not
        #clear_output(wait=True)
        print("\n---------Access Granted---------")
        while True: #giving an extra chance for the user until he chooses to end the program
            print("\n\n--> ENTER 1 TO CALCULATE YOUR BMI.\n--> ENTER 2 TO KNOW YOUR DISEASE CAUSED ACCORDING TO BMI CATEGORY.\n--> ENTER 3 TO EXIT.")
            choice=input(" \n--> ENTER YOUR CHOICE : ")
            switch(choice)
            
    else: #if otp doesn't match generate a new otp and give a chance to enter th otp
        #clear_output(wait=True)
        print("Sorry, your OTP is seems to be wrong !\n\n---------Access Denied---------")
        otp=random.randint(1111,9999)
        print("\nWe have generated an OTP for you to access the calculator:\nYOUR OTP IS ",otp)
