print("Welcome to Study Tracker")

study_history = {}

while True: 
    print("\n1. Enter Study Session Stats")
    print("2. View Study History")
    print("3. Set Study Goal")
    print("4. Exit")

    choice = input("Enter your choice between 1 and 4: ")
     
    if choice == "1":
        subject = input("Enter the subject: ").capitalize()
        hours = int(input("Enter study hours: "))
        study_method = input("Enter Style of Studying: ")
        print("Your study session has been entered.")
        
        if subject in study_history:
            print("You already studied this subject. Updating total hours.")
            study_history[subject] = study_history[subject] + hours
        else:
            study_history[subject] = hours

        print("Your study session has been entered.")

    elif choice == "2":
        print("\nStudy History:")
        for subject , hours in study_history.items():
            print(subject, ":", hours, "hours")
    elif choice == "3":
        study_goal = int(input("Enter your total study hour goal: "))

        total_hours = 0
        for subject in study_history:
         total_hours = total_hours + study_history[subject]

        print("Your study goal is", study_goal, "hours.")
        print("You have studied", total_hours, "hours so far.")

        if total_hours >= study_goal:
           print("You reached your study goal!")
        else:
           print("You need", study_goal - total_hours, "more hours to reach your goal.")
