def calculate(weight,height): #funtion to calculate bmi and print their condition
    bmi = (float(weight)/(float(height)/100)**2) #typecasting the weight and height variables to float
    if bmi < 16:  
        print("\n--> Oops! You are underweight - Severe Thinness.\nBMI : ",round(bmi,1))  
        bcat="Starvation"
    elif bmi < 17:  
        print("\n--> Oops! You are underweight - Moderate Thinness.\nBMI : ",round(bmi,1))  
        bcat="Anorexic"
    elif bmi < 18.5:  
        print("\n--> Oops! You are underweight - Mild Thinness.\nBMI : ",round(bmi,1))  
        bcat="Underweight"
    elif bmi < 25:  
        print("\n--> Awesome! You are healthy.\nBMI : ",round(bmi,1))
        bcat="Ideal"
    elif bmi < 30:  
        print("\n--> Eee! You are overweight.\nBMI : ",round(bmi,1))
        bcat="Overweight"
    elif bmi < 35:  
        print("\n--> Eee! You are Obese - Obese Class 1.\nBMI : ",round(bmi,1))
        bcat="Obese"
    elif bmi < 40:  
        print("\n--> Eee! You are Obese - Obese Class 2.\nBMI : ",round(bmi,1))  
        bcat="Morbidly Obese"
    category=[
        ["\n Your BMI category is : ",bcat]
    ]
    print(tabulate(category))
    #printing details and BMI of the user in tabular form
    mylist = [
    ["| 1.","Name : ", name,"|"],
    ["| 2.","Gender : ", gender,"|"],
    ["| 3.","Age : ", age,"|"],
    ["| 4.","BMI : ",round(bmi,1),"|"]   
    ]
    print(tabulate(mylist))
