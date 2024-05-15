import sqlite3
import time

db_connection = sqlite3.connect("sql-murder-mystery.db")
db_cursor = db_connection.cursor()

#other ideas: wrapping text? idk

#interactive functions: -----------------------------------------     
def introduction():
    print("•───────•°•❀•°•───────•\n")
    print("Hi! We're building a text-based game :3\n")
    print("═════════•°• ⚠ •°•═════════\n")
    print("There's been a murder in SQL City!")
    print("Can we find out who did it?\n")
    input("Press any key to continue...")

def crime_scene_report():
    print("Let's start with looking at the crime scene reports!\n")

    print("There are different types of crimes listed in the report:")
    print(f"{report_types()}.\n")
    time.sleep(2)

    crime = input("What type of crime are we looking for? Please type the answer exactly how it is in the list above: ")
    crime_answer(crime)
    time.sleep(1)

    input("Press any key to continue...")
    print("\n")
    #time.sleep(3)

    print("The crime scene report lists crimes from a variety of cities:")
    time.sleep(2)
    print(f"{city_types()}.\n")
    time.sleep(2)

    print("I'm sorry, I know, that was A LOT.")
    print("Let's think of it as something like Where's Waldo! (Again, I'm so sorry). But, a hint: The answer is also in our little introduction :)\n")
    time.sleep(2)

    city = input("In which city are we looking for murders? Please type the answer exactly how it is in the list above: ")
    city_answer(city)
    time.sleep(1)

    input("Press any key to continue...")
    print("\n")
    #time.sleep(2)

    print("I promise nothing else will be as bad as that was.\n")
    time.sleep(3)

    print("Now, let's see the reports for murders in SQL City!\n")
    time.sleep(2)
    cs_report_filtered()
    time.sleep(2)

    print("Report #2 has provided us with some information about the witnesses. Let's try to find out who they are!\n")
    time.sleep(1)

    input("Press any key to continue...")
    time.sleep(3)

def witness():
    print("The first witness lives at the last house on Northwestern Dr.\n")
    time.sleep(2)

    print("Don't worry, I promised nothing else would be as bad as the list of cities.\n")
    time.sleep(2)

    print("So! Here are 5 (AND ONLY 5!!) people who live on Northwestern Dr, sorted by address number in descending order:\n")
    time.sleep(2)

    witness_one()
    time.sleep(2)

    first_witness = input("Who is our first witness? Enter their full name: ")
    witness_one_answer(first_witness)
    #time.sleep(3)
    time.sleep(1)
    input("Press any key to continue...")
    print("\n")

    print("We know two things about our second witness: their first name is Annabel and they live on Franklin Ave.\n")
    time.sleep(2)

    print("Let's look at some people who live on Franklin Ave: \n")
    time.sleep(2)

    witness_two()
    time.sleep(2)

    second_witness = input("Who is our second witness? Enter their full name: ")
    witness_two_answer(second_witness)
    time.sleep(1)
    input("Press any key to continue...")

    time.sleep(3)

def witness_interview():
    print("Now that we know who our witnesses are, let's see what they said in their investigative interviews.\n")
    time.sleep(2)

    print("Let's start with Morty's...\n")
    time.sleep(2)
    witness_one_interview()
    time.sleep(2)

    print("Let's see what Annabel has to say...\n")
    time.sleep(2)
    witness_two_interview()
    time.sleep(1)

    input("Press any key to continue...")

    time.sleep(3)

def gym():
    print("It looks like we'll need to go through some of the records at the Get Fit Now Gym.\n")
    time.sleep(2)

    print("Morty said our suspect's membership number included '48Z', and mentioned that they have to be a gold member.")
    time.sleep(2)

    print("Let's look at everyone who fits that criteria.\n")
    time.sleep(2)

    gym_members_gold()
    time.sleep(3)

    print("Annabel said that the suspect was there on the 9th of January.")
    time.sleep(2)

    print("Let's see who went to the gym that day...\n")
    time.sleep(2)
    gym_members_date()

    time.sleep(3)

    print("Last but not least, Morty also said that the suspect's license plate included the characters 'H42W'.")
    time.sleep(2)

    print("Let's look at some license plates...\n")
    time.sleep(2)

    gym_suspect_license()
    #time.sleep(1)

    #input("Press any key to continue...")
    time.sleep(3)

def final_suspect():
    suspect = input("Using all this information, can you determine who our suspect is? Enter their full name: ")
    suspect_answer(suspect)
    time.sleep(3)

    print("Let's see what Jeremy had to say in his investigative interview: \n")
    time.sleep(2)
    suspect_interview()

    time.sleep(3)
    
def intermission():
    print("You have found the prime suspect. You can choose to keep going to find the criminal behind all of this, or end here.\n")
    time.sleep(2)
    proceed = int(input("Would you like to keep going, or end here? Enter 1 to continue, or 2 to end: "))
    keep_going(proceed)
    
def true_criminal():
    print("Jeremy said that the person behind this went to a particular event three times in December.")
    time.sleep(2)
    event = input("What is the name of this event? Note that the answer is case-sensitive: ")
    event_answer(event)
    time.sleep(2)

    print("Here is a list of the people who attended the SQL Symphony in December: \n")
    time.sleep(2)
    event_count()
    time.sleep(2)

    #input("Press any key to continue...")
    #print("\n")
    
    print("And using Jeremy's interview, let's look at some car records: \n")
    time.sleep(2)
    criminal_car()
    time.sleep(1)

    input("Press any key to continue...")
    print("\n")
    time.sleep(2)

    print("You can probably tell who the true criminal is now.")
    criminal = input("Who is it? Enter their full name: ")
    criminal_answer(criminal)

    time.sleep(3)
    print("Jeremy said that Miranda has a lot of money. Just for fun, let's see how much she earns: \n")
    time.sleep(2)

    miranda_earnings()
    time.sleep(2)

    print("...Jeremy was right.\n")

def conclusion():
    print("Well... that's all, folks!")
    time.sleep(1)
    print("Thanks for playing!\n")
    time.sleep(1)

    print("I don't have any prizes to give, but...")
    time.sleep(1)
    print("Idk man here's Shrek because why not")
    time.sleep(1)

    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊⠉⠀⠀⠀⠀⠀⠀⠈⠁⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠇⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠶⠿⠶⣄⡈⠂⠔⠀⠀⠈⠀⠀⠈⠉⠻⣦⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡘⡀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡆⠀⠀⠀⠀⠒⣉⣉⠛⢿⣿⣿⣄⠀⢀⣠⣤⣶⡾⠛⠋⠙⠁⣀⠔⠁⣠⣬⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⠀⠀⠐⠁⢞⣯⠎⣸⠿⠛⠉⠀⠘⢿⣟⢭⣭⡅⠀⠀⠀⠀⡠⠚⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣀⡀⠀⠀⢀⣠⣤⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠜⠻⠃⠀⠀⠀⠰⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣀⣀⣤⣼⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⣠⣤⣤⣤⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⣶⣶⣿⣿⣿⡀⠀⠀⠀⠀⠀
    ⠠⠔⠒⠉⠉⠀⠈⠉⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⢀⣼⠟⠛⠛⠛⠛⠻⢿⣷⣤⣄⣀⣠⣤⡶⠦⠤⡀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⠟⠛⠉⠁⠒
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠉⠁⠀⠀⠀⠈⢳⣆⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⠈⠀⠐⣶⣿⣿⠿⣿⠖⢦⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠻⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠸⣿⣿⣇⣿⣀⡈⠀⠀⠋⠉⠙⠛⠛⢲⣦⠤⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣷⣶⣾⣶⣿⡿⠃⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠻⣿⣄⡉⠙⠛⠛⠛⠛⢻⡿⠋⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠈⠉⠛⠻⠷⠶⠶⠒⠉⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠲⣤⣤⣤⣤⣴⣾⣿⡿⠟⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠉⠉⠉⠉⠉⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⠢⠤⠤⠤⠤⠔⠊⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀
    ⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠉⠛⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)

    print("\n")
    time.sleep(1)
    print("Anyways that's all for real now bye bye\n")
    time.sleep(1)

    input("Press any key to exit...")
    exit()

# the end! or is it...

#query functions: ---------------------------------------  
def report_types():
    db_cursor.execute("SELECT DISTINCT type FROM crime_scene_report ORDER BY type ASC")
    types = db_cursor.fetchall()
    all_types = []
    for category in types:
        all_types += [category[0]]
    all_types = ", ".join(all_types)
    all_types = all_types.capitalize()
    return all_types

def city_types():
    db_cursor.execute("SELECT DISTINCT city FROM crime_scene_report ORDER BY city ASC")
    cities = db_cursor.fetchall()
    all_cities = []
    for place in cities:
        all_cities += [place[0]]
    all_cities = ", ".join(all_cities)
    return all_cities

def crime_answer(crime):
    if crime == "murder":
        print("Correct! We're looking for murders.\n")
        return
    else:
        print("Wrong choice! Let's try again.")
        crime = input("What type of crime are we looking for? ")
        crime_answer(crime)

def city_answer(city):
    if city == "SQL City":
        print("Correct! We're looking for murders in SQL City!\n")
        return
    else:
        print("Hm, not quite. Let's try again.")
        city = input("In which city are we looking for murders? ")
        city_answer(city)

def cs_report_filtered():
    db_cursor.execute("SELECT * FROM crime_scene_report WHERE type = 'murder' AND city = 'SQL City'")
    reports = db_cursor.fetchall()
    count = 1
    for row in reports:
        print(f"Report #{count}")
        print(f"Date: {row[0]}\nType: {row[1]}\nDescription: {row[2]}\nCity: {row[3]}\n")
        count+=1        

def witness_one():
    db_cursor.execute("SELECT * FROM person WHERE address_street_name = 'Northwestern Dr' ORDER BY address_number DESC LIMIT 5")
    north_people = db_cursor.fetchall()
    count = 1
    for row in north_people:
        print(f"#{count}:")
        print(f"ID #: {row[0]}\nName: {row[1]}\nLicense ID #: {row[2]}\nAddress #: {row[3]}\nStreet Name: {row[4]}\nSSN: {row[5]}\n")
        count += 1

def witness_one_answer(first_witness):
    if first_witness == "Morty Schapiro":
        print("Yep! Morty Schapiro is our first witness.\n")
        return
    else:
        print("No, wrong answer. Let's try again.")
        first_witness = input("Who is our first witness? ")
        witness_one_answer(first_witness)

def witness_two():
    db_cursor.execute("SELECT * FROM person WHERE address_street_name = 'Franklin Ave' ORDER BY name ASC LIMIT 5")
    frank_people = db_cursor.fetchall()
    count = 1
    for row in frank_people:
        print(f"#{count}:")
        print(f"ID #: {row[0]}\nName: {row[1]}\nLicense ID #: {row[2]}\nAddress #: {row[3]}\nStreet Name: {row[4]}\nSSN: {row[5]}\n")
        count += 1

def witness_two_answer(second_witness):
    if second_witness == "Annabel Miller":
        print("Yep! Annabel Miller is our second witness.\n")
        return
    else:
        print("No, wrong answer. Let's try again.")
        second_witness = input("Who is our first witness? ")
        witness_two_answer(second_witness)

def witness_one_interview():
    db_cursor.execute("SELECT p.name, i.transcript FROM person AS p JOIN interview AS i ON p.id = i.person_id WHERE p.name = 'Morty Schapiro'")
    interview_one = db_cursor.fetchall()
    for row in interview_one:
        print(f"Name: {row[0]}\nInterview Transcript: {row[1]}\n")

def witness_two_interview():
    db_cursor.execute("SELECT p.name, i.transcript FROM person AS p JOIN interview AS i ON p.id = i.person_id WHERE p.name = 'Annabel Miller'")
    interview_two = db_cursor.fetchall()
    for row in interview_two:
        print(f"Name: {row[0]}\nInterview Transcript: {row[1]}\n")

def gym_members_gold():
    db_cursor.execute("SELECT id, name, membership_start_date, membership_status FROM get_fit_now_member WHERE id LIKE '%48Z%' AND membership_status = 'gold'")
    gold_members = db_cursor.fetchall()
    for row in gold_members:
        print(f"Member ID: {row[0]}\nName: {row[1]}\nMembership Start Date: {row[2]}\nMembership Status: {row[3]}\n")

def gym_members_date():
    db_cursor.execute("SELECT * FROM get_fit_now_check_in WHERE check_in_date = 20180109")
    date_members = db_cursor.fetchall()
    for row in date_members:
        print(f"Member ID: {row[0]}\nCheck In Date: {row[1]}\nCheck In Time: {row[2]}\nCheck Out Time: {row[3]}\n")

def gym_suspect_license():
    db_cursor.execute("SELECT gender, plate_number, car_make, car_model FROM drivers_license WHERE plate_number LIKE '%H42W%'")
    license_plates = db_cursor.fetchall()
    for row in license_plates:
        print(f"Sex: {row[0]}\nLicense Plate Number: {row[1]}\nCar Make: {row[2]}\nCar Model: {row[3]}\n")

def suspect_answer(suspect):
    if suspect == "Jeremy Bowers":
        print("Congratulations! You found our prime suspect, who is indeed Jeremy Bowers.\n")
        return
    else:
        print("Ouch! Incorrect answer. Let's try again.")
        suspect = input("Who is our first witness? ")
        suspect_answer(suspect)

def suspect_interview():
    db_cursor.execute("SELECT p.name, i.transcript FROM person AS p JOIN interview AS i ON p.id = i.person_id WHERE p.name = 'Jeremy Bowers'")
    interview_one = db_cursor.fetchall()
    for row in interview_one:
        print(f"Name: {row[0]}\nInterview Transcript: {row[1]}\n")

def keep_going(proceed):
    if proceed == 1:
        print("Okay! Let's keep going. ^_^\n")
        time.sleep(1)
        input("Press any key to continue...")
        return
    elif proceed == 2:
        input("Okay! Press any key to exit...")
        exit()
    elif proceed != 1 and proceed != 2:
        proceed = int(input("Invalid input. Please try again: "))
        keep_going(proceed)

def event_answer(event):
    if event == "SQL Symphony":
        print("You're right! We're looking for someone who went to the SQL Symphony three times in December.\n")
        return
    else:
        print("Not quite. Let's try again.")
        event = input("What is the name of this event? ")
        event_answer(event)

def event_count():
    db_cursor.execute("SELECT p.name, p.license_id, COUNT(e.person_id) AS frequency FROM person AS p JOIN facebook_event_checkin AS e ON p.id = e.person_id WHERE date LIKE '201712%' AND event_name = 'SQL Symphony Concert' GROUP BY e.person_id;")
    guest_list = db_cursor.fetchall()
    for row in guest_list:
        print(f"Name: {row[0]}\nLicense ID: {row[1]}\nFrequency: {row[2]}\n")

def criminal_car():
    db_cursor.execute("SELECT * FROM drivers_license WHERE gender = 'female' AND car_make = 'Tesla' AND car_model = 'Model S' AND hair_color = 'red'")
    car_records = db_cursor.fetchall()
    for row in car_records:
        print(f"License ID: {row[0]}\nAge: {row[1]}\nHeight: {row[2]}\nEye Colour: {row[3]}\nHair Colour: {row[4]}\nSex: {row[5]}\nLicense Plate Number: {row[6]}\nCar Make: {row[7]}\nCar Model: {row[8]}\n")

def criminal_answer(criminal):
    if criminal == "Miranda Priestly":
        print("Yes! We did it! Miranda Priestly is in fact the mastermind behind this whole scheme.\n")
        return
    else:
        print("Come on, you can do this. Let's try again.")
        criminal = input("Who is it? ")
        criminal_answer(criminal)

def miranda_earnings():
    db_cursor.execute("SELECT p.name, m.annual_income FROM person AS p JOIN income AS m ON p.ssn = m.ssn WHERE p.name = 'Miranda Priestly';")
    annual_earnings = db_cursor.fetchall()
    for row in annual_earnings:
        print(f"Name: {row[0]}\nAnnual Income: {row[1]}\n")

#execution: ------------------------------------------
introduction() 
print("\n")
crime_scene_report()
print("\n")
witness()
witness_interview()
gym()
final_suspect()
intermission()
true_criminal()
conclusion()
    
# have a cookie idk nom nom 🍪
# something something graphical implementation? tkinter? idk man when we reach that bridge we'll cross it // update: we are NOT crossing that bridge man i am TIRED