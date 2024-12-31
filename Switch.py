#Switching the choice as per users input
def switch(choice):
    #clear_output(wait=True)
    if choice==str("1"):
        calculate(weight,height)#calculating bmi
    elif choice==str("2"):
        #Displaying the details of their bmi category
        #clear_output(wait=True)
        #print("YOUR BMI CATEGORY IS ",bcat)
        print("\nSELECT YOUR BMI CATEGORY TO KNOW THE DISEASE FORM WHICH A PERSON OF THAT SPECIFIC BMI CATEGORY CAN BE EFFECTED - ")
        print("\n1 - STARVATION\n2 - ANOREXIC\n3 - UNDERWEIGHT\n4 - IDEAL\n5 - OVERWEIGHT\n6 - OBESE\n7 - MORBIDLY OBESE\n8 - SEVERELY OBESE\n")
        cat=input("\nENTER THE NUMBER OF YOUR BMI CATEGORY : ") #Reading BMI category to print the category details
        if cat==str("1"):
            #clear_output(wait=True)
            print("\nAccording to your BMI category there is a chance of being effected by diabetes.\n\n Symptoms - \nExcessive thirst , urination, fatigue, weight loss  blurred vision\n\nHow it occurs - It occurs when your blood glucose, also called blood sugar, is too high.Diet - coffee, pumpkin seeds, berries, yogurt,  nuts, beans, poultry, fish\n\n Precautions - \t1)Exercise regularly.\n \t\t2)Manage your carb intake.\n \t\t3)Eat more fiber.\n\t\t4)Drink water and stay hydrated.\n \t\t5)Implement portion control.\n \t\t6)Choose foods with a low glycemic index.\n\t\t7)Try to manage your stress levels.\n \t\t8)Monitor your blood sugar levels.\n\nVitamins and minerals needed - vitamin C (1-3 grams per day), vitamin B, Chromium, Magnesium\n\n")
        elif cat==str("2"):
            #clear_output(wait=True)
            print("\nAccording to your BMI category there is a chance of being effected by depression.\n\n Symptoms - \n 1. Feelings of sadness, tearfulness, emptiness or hopelessness.\n 2. Anger outbursts, irritability or frustration, even over small matters.\n 3. Loss of interest or pleasure in most or all normal activities, such as hobbies or sports.\n 4. Sleep disturbances, including insomnia or sleeping too much.\n\nHow it occurs - It can occur for a variety of reasons an upsetting or stressful life event, such as bereavement, divorce, illness, redundancy and job or money worries , etc.\n\nDiet - oysters and mussels, other seafood, lean organ meats, leafy greens, lettuce, peppers, and cruciferous vegetables such as broccoli, cauliflower, cabbage, kale, and Brussels sprouts.\n\nPrecautions -\t1. Exercise regularly.\n\t\t2. Cut back on social media time.\n \t\t3. Build strong relationships.\n \t\t4. Minimize your daily choices.\n \t\t5. Reduce stress.\n\n  Vitamins and minerals needed - vitamin B3 , B9 , C and D , omega 3 fatty acids and magnesium.\n\n")
        elif cat==str("3"):
            #clear_output(wait=True)
            print("\nAccording to your BMI category there is a chance of being effected by Anemia.\n\n Symptoms - \nFatigue, skin pallor, shortness of breath, light-headedness, dizziness or a fast heartbeat.\n\nHow it occurs - Anemia occurs when your blood doesn't have enough red blood cells. This can happen if: Your body doesn't make enough red blood cells.\n\nDiet - Broccoli , Grapefruit , Kiwi , Leafy greens , Melons , Oranges , Peppers ,Strawberries ,Tangerines ,Tomatoes.\n\nPrecautions - Eat plenty of iron-rich foods, such as tofu, green and leafy vegetables, lean red meat, lentils, beans and iron-fortified cereals and breads. Eat and drink vitamin C-rich foods and drinks. Avoid drinking tea or coffee with your meals, as they can affect iron absorption.\n\nVitamins and minerals needed - vitamin C , Vitamin B12.\n\n")
        elif cat==str("4"):
            #clear_output(wait=True)
            print("\nyou're perfect")
        elif cat==str("5"): 
            #clear_output(wait=True)
            print("\nAccording to your BMI category there is a chance of being effected by Gout.\n\n Symptoms - \nPain in the zoints of leg, deformity at base of big toe or thick skin at base of big toe, stiffness or swelling,redness or tenderness\n\nHow it occurs -  It occurs when some of the bones in the front part of your foot move out of place. This causes the tip of your big toe to get pulled toward the smaller toes and forces the joint at the base of your big toe to stick out.\n\nDiet - eggs, beans/lentils, seeds/nuts, fish, poultry, tofu, yogurt, antioxidants rich foods and phytochemicals\n\nPrecautions  -\t1)Keep track of the shape of your feet as they develop over time, especially if bunions run in your family\n\t\t2)Exercising the feet can strengthen them\n \t\t3)Wear shoes that fit properly and don't cramp or pinch your toes\n \t\t4)Women should avoid shoes with high heels or pointed toes\n \t\t5)Try Bunion Pads\n \t\t6)Soak Your Feet in a Foot Bath\n \t\t7)avoid sugary soft drinks and food, junk food\n\n Vitamins and minerals needed -Vitamin C, Selenium, Carotenes, and Bioflavonoids.\n\n")
        elif cat==str("6"):
            #clear_output(wait=True)
            print("\nAccording to your BMI category there is a chance of being effected by Brain Stroke.\n\n Symptoms - \nMuscle weakness or numbness , balance disorder, difficulty swallowing, headache, inability to understand, mental confusion, or rapid involuntary eye movement .\n\nHow it occurs - Blocked artery (ischemic stroke) or leaking or bursting of a blood vessel (hemorrhagic stroke). Some people may have only a temporary disruption of blood flow to the brain.\n\nDiet -\t1. Avoid Processed Foods, Salt, and Sugar.\n\t\t2. Eat More Legumes.\n\t\t3. Eat Fish and Poultry Instead of Red Meat.\n\t\t4. Avoid Saturated Fat and Snack on Seeds and Nuts.\n\nPrecautions - Limit foods high in saturated fat such as biscuits, cakes, pastries, pies, processed meats, commercial burgers, pizza, fried foods, potato chips, crisps and other savoury snacks. Limit foods which contain mostly saturated fats such as butter, cream, cooking margarine, coconut oil and palm oil.\n\nVitamins and minerals needed - vitamin D , probiotics , Vitamin B3 , vitamin B12 , DHA , vitamin C.\n\n")
        elif cat==str("7"):
            #clear_output(wait=True)
            print("\nAccording to your BMI category there is a chance of being effected by High Colestrol.\n\n Symptoms - \nHeart attack, peripheral artery disease, or stroke .\n\nHow it occurs - Eating too many foods that are high in fat can increase your cholesterol level. Being overweight and inactive also causes high cholesterol\n\nDiet - green leafy vegetables, avocados, apples,  oranges,  bananas\n\nPrecautions -\t1) Eat a low-salt diet that emphasizes fruits, vegetables and whole grains.\n\t\t2)Limit the amount of animal fats and use good fats in moderation.\n\t\t3)Lose extra pounds and maintain a healthy weight.\n\t\t4)Quit smoking.\n\t\t5)Exercise on most days of the week for at least 30 minutes.\n\nVitamins and minerals needed -Vitamin B, Niacin, Phytosterols, Soluble fiber.\n\n")
    elif choice==str("3"):
        #quiting the program 
        #clear_output(wait=True)
        print("\n\n\t--------------------------------------------")
        print("\t\t         THANK YOU ")
        print("\t--------------------------------------------\n\n\n")
        exit()
