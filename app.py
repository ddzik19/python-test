# I am going to use json as a database therefore we
# need to import json
import json

# I have created our cars database, the first two cars had the same id of 1 therefore 
# I changed the second cars id in the array to 6 as we have six cars and the other cars
# already have a unique id.
cars ="""
    {
        "cars":[{
        "make":"Nissan",
        "model":"Micra",
        "year":2004,
        "chassis_no":"12345A",
        "id":1,
        "last_updated":"2017-02-01 00:00:00",
        "price":500.0
    },{
        "make":"Nissan",
        "model":"Micra",
        "year":2004,
        "chassis_no":"12425A",
        "id":6,
        "last_updated":" 2017-03-01 00:00:00",
        "price":400.0
    },{
        "make":"Ford",
        "model":"Fiesta",
        "year":2002,
        "chassis_no":"12345B",
        "id":2,
        "last_updated":" 2017-03-01 00:00:00",
        "price":300.0
    },{
        "make":"Audi",
        "model":"A3",
        "year":"",
        "chassis_no":"12345C",
        "id":3,
        "last_updated":" 2017-04-01 00:00:00",
        "price":0
    },{
        "make":"Nissan",
        "model":"Micra",
        "year":"2004",
        "chassis_no":"12345D",
        "id":4,
        "last_updated":" 2017-05-01 00:00:00",
        "price":200.0
    },{
        "make":"Peugot",
        "model":"308",
        "year":"1998",
        "chassis_no":"12345E",
        "id":5,
        "last_updated":" 2017-06-01 00:00:00",
        "price":100.0
    }]
    }
    """

# we parse the cars json
data = json.loads(cars)

# the main app function 
def main():
    # creating a boolean that will be responsible for 
    # the continuous dispalying of the menu until the
    # user exits the app
    isRunning = True
    # while loop responsible for running the app
    while isRunning:
        # displaying the menu to the suer
        menu()
        
        try:
            # getting user inputs
            userInput = int(input("Please enter option: "))
        except ValueError:
            print("Value entered is not a number. Please enter a number.")
            continue
        
        # checking for inputs
        if userInput == 1:
            try:
                carid = int(input("Please enter id of car to get: "))
            except ValueError:
                print("Value is not a number, Please try again.")
                continue
            carById(carid)
        elif userInput == 2:
            # displaying teh sub menu
            averagePriceSubMenu()
            # try block to validate if entered option is number
            try:
                option = int(input("Please enter option: "))
            except ValueError:
                print("Value is not a number, Please try again.")
            if option == 1:
                # execute the getAverageByMake function
                getAverageByMake()
        elif userInput == 0:
            print("Goodbye!")
            isRunning = False

# this function will be responsible for displaying the menu to the user
def menu():
    # printing the menu with a nice margin that makes the menu easy to read
    print("""
        ----------------------------
        | Menu                     |
        ----------------------------
        | 1. List car by id        |
        | 2. Average price of car  |
        ----------------------------
        | 0. Exit                  |
        ----------------------------
        """)

# this function will be responsible for getting a car by id
def carById(id):
    # looping through the cars in the json array
    for car in data['cars']:
        # if the id of the car in the array matches the 
        # passed in id we will display the information
        # else we will display an error message
        if car['id'] == id:
            # printing the information
            print("""
        ----------------------------------------
        | Information                          |
        ----------------------------------------
        | Make: {}                                
        | Model: {}                               
        | year: {}                                
        | id: {}                                  
        | last_updated: {}                        
        | price: {}                               
        ----------------------------------------
                  """.format(car['make'],car['model'],car['year'],car['id'],car['last_updated'],car['price']))
            break
    else:
        print("Car with this id does not exist.")

# this is a sub menu that will be displayed when the user enters option 2        
def averagePriceSubMenu():
    # printing a submenu
    print("""
          -------------------------------
          | Get average price by:       |
          -------------------------------
          | 1. Make                     |
          | 2. Model                    |
          -------------------------------
          """)           

def getAverageByMake():
    
    # creating empty list
    makeList = []
    # creating a list that will hold the unique car makes
    finalList = []
    # we will now iterate through the cars and add the models to the make
    for car in data['cars']:
        makeList.add(car['make'])
    
    # now we want to get unique makes
    for i in makeList:
        # if i is not in finalList we add it to finalList
        # this means we will only have unique makes in finallist
        if i not in finalList:
            finalList.append(i)
        
    print(finalList)
# running the main function
main()