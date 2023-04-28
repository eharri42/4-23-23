import urllib
import requests


answer = input( " Welcome, do you want to play a game? Type (Yes/No).")
if answer.lower().strip() == "no":
        print("Game Over.")

if answer.lower().strip() == "yes":
 print("Great, what is your name?")
 user_name = input()
 print("Okay", user_name, "You've decided to help your friend test out his programming escape room. He said he made it simple to start and would appreciate some feedback.")
 print("You arrive to the house at dawn, your friend explains that you need a key to exit and places you in the room.")
 print("Once in the room you look around, the room is large, it has a small black filing cabinet placed in a corner on the left,")
 print("a bookshelf is directly in front of you, pushed against the wall. All 4 shelves of the bookcase are crammed with books.")
 print("Several chairs and a small loveseat fill up the remaining space in the room, with a computer desk, desk chair,")
 print("and a printer pushed up against the wall to the right.")
answer = input("What do you go to first? 1. The file cabinets 2. The bookcase. 3. The furniture. 4. The computer. Type your number now.")
if answer == "1":
    print("You open the file cabinet but there's nothing inside")
answer = input(" Where else would you like to go? 2. The bookcase. 3. The furniture. 4. The computer. Type your number now.")
if answer == "2":
    print("There may be over a hundred books on the shelfs and the topics seem random, none to due with computers at first glance.")
    answer = input(" Where else would you like to go? 2. The bookcase. 3. The furniture. 4. The computer. Type your number now.")
if answer == "3":
    print("You search the furniture but you don't find any clues or a key.")
    answer = input(" Where else would you like to go? 2. The bookcase. 3. The furniture. 4. The computer. Type your number now.")
    if answer == "4":
        print("You walk over to the computer and sit down. There is a piece of paper on the table that says 'You have four tasks',")
        print("Write a program that tells what 28 days from today would be, then link to a weather forecast site for the day in question, a")
        print(" link to the weather forecast site for a week later. Write a problem that pulls air quailty reports for the day of.")
        print("The computer is already on with just three visible icons on the desktop. A browser, an IDE, and the symbol for settings. ")
        print("You open up the IDE and write the programs. Write a for loop that ends a 5 and prints the words 'Done with loop'")
    #Module #1.
        import datetime
        today = datetime.date.today()
        days_from_now = int(input('Enter number of days from now: '))
        day_difference = datetime.timedelta(days=days_from_now)
        future_date = today + day_difference
        print(f'{days_from_now} days from now is {future_date.strftime("%B %d, %Y")}')

    #Module #2
        from urllib import request
        from urllib.request import Request, urlopen

        url = "https://www.weather25.com/north-america/usa?page=date&date=20-4"
        request_site = Request(url, headers={"User-Agent": "Mozilla/5"})
        webpage = urlopen(request_site).read()
        print(webpage[:500])

    #Module #3
        from urllib import request
        from urllib.request import Request, urlopen

        url = "https://www.weather25.com/north-america/usa?page=date&date=30-4"
        request_site = Request(url, headers={"User-Agent": "Mozilla/5"})
        webpage = urlopen(request_site).read()
        print(webpage[:500])

    #API
        import requests
        url = "https://air-quality-by-api-ninjas.p.rapidapi.com/v1/airquality"
        querystring = {"city": "Grand Rapids"}
        headers = {
            "X-RapidAPI-Key": "ed8d85dacemsha9218e9b2ade5dcp16b438jsnaa7bedccac8d",
            "X-RapidAPI-Host": "air-quality-by-api-ninjas.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
    #While loop
    i =1
    while i<= 5:
        print(i)
        i += 1
    print("Done with loop")
print("Once you finish the last program you hear a popping sound, it sounds like it came from under the desk. You look and see a small compartment that has popped open.")
print("You pull out a key from inside. You hear the sound of an intercom turning on and your friend congratulates you on finishing the room.")
