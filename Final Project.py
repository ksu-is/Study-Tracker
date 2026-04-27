print("Welcome to Study Tracker")

study_history = {}

while True: 
    print("\n1. Enter Study Session Stats")
    print("2. View Study History")
    print("3. Exit")

    choice = input("Enter your choice between 1 and 3")
     
    if choice == "1":
        subject = input("Enter the subject: ").capaitalize()
        hours = int(input("Enter study hours: "))
        study_method = str(input("Enter Style of Studying: "))

        study_history[subject] = hours
        print("Your study session has been entered.")
          if subject in study_history:
            print("You already studied this subject. Updating total hours.")
            study_history[subject] = study_history[subject] + hours
        else:
            study_history[subject] = hours

        print("Your study session has been entered.")
