questions = {
    "1. How often do you eat beef?":['a. Never', 'b. 1-2 times a week', 'c. 3-5 times a week', 'd. Once a day', 'e.'],
    "2. How often do you eat chicken?":['a. Never', 'b. 1-2 times a week', 'c. 3-5 times a week', 'd. Once a day', 'e.'],
    "3. How often do you eat pork?":['a. Never', 'b. 1-2 times a week', 'c. 3-5 times a week', 'd. Once a day', 'e.'],
    "4. How often do you eat lamb?":['a. Never', 'b. 1-2 times a week', 'c. 3-5 times a week', 'd. Once a day', 'e.'],
    "5. How often do you eat fish?":['a. Never', 'b. 1-2 times a week', 'c. 3-5 times a week', 'd. Once a day', 'e.'],
} 
gas_emissions = 0 
land_usage = 0
water_usage = 0

for question_number,question in enumerate(questions): 
    print ("Question", question_number+1) 
    print(question_number)
    print (question)
    for options in questions[question][:-1]: 
        print(options)
    user_choice = input("Answer: ")

    #question 1, eating beef 
    if question_number+1 == 1:
        if user_choice == 'a':
            gas_emissions += 0
            land_usage += 0
            water_usage += 0
        elif user_choice == 'b': 
            gas_emissions += 604 
            water_usage += 102388
            land_usage += 1735
        elif user_choice == 'c':
            gas_emissions += 1611
            water_usage += 273104
            land_usage += 4625
        elif user_choice == 'd':
            gas_emissions += 2820
            water_usage += 477880
            land_usage += 8094

    #for question 2, eating chicken
    if question_number+1 == 2:
        if user_choice == 'a':
            gas_emissions += 0
            land_usage += 0
            water_usage += 0
        elif user_choice == 'b': 
            gas_emissions += 106
            water_usage += 7134
            land_usage += 0
        elif user_choice == 'c':
            gas_emissions += 284
            water_usage += 19025
            land_usage += 0
        elif user_choice == 'd':
            gas_emissions += 497
            water_usage += 33294
            land_usage += 0


    #for question 3, eating pork
    if question_number+1 == 3:
        if user_choice == 'a':
            gas_emissions += 0
            land_usage += 0
            water_usage += 0
        elif user_choice == 'b': 
            gas_emissions += 140
            water_usage += 20519
            land_usage += 0
        elif user_choice == 'c':
            gas_emissions += 375
            water_usage += 54718
            land_usage += 0
        elif user_choice == 'd':
            gas_emissions += 656
            water_usage += 95756
            land_usage += 0

    #for question 4, eating lamb
    if question_number+1 == 4:
        if user_choice == 'a':
            gas_emissions += 0
            land_usage += 0
            water_usage += 0
        elif user_choice == 'b': 
            gas_emissions += 339
            water_usage += 69212
            land_usage += 3157
        elif user_choice == 'c':
            gas_emissions += 904
            water_usage += 230672
            land_usage += 8419
        elif user_choice == 'd':
            gas_emissions += 1582
            water_usage += 322920
            land_usage += 14733
    
    #for question 5, eating fish
    if question_number+1 == 5:
        if user_choice == 'a':
            gas_emissions += 0
            land_usage += 0
            water_usage += 0
        elif user_choice == 'b': 
            gas_emissions += 146
            water_usage += 39646
            land_usage += 0
        elif user_choice == 'c':
            gas_emissions += 390
            water_usage += 19025
            land_usage += 0
        elif user_choice == 'd':
            gas_emissions += 683
            water_usage += 185013
            land_usage += 0

    

    
print("Your eating habits release " + str(gas_emissions) + " kg of greenhouse gases annually.")
print("Your eating habits waste " + str(water_usage) + " liters of water annually.")
print("Your eating habits use up " + str(land_usage) + " meters squared of land annually.")
