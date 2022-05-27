# python-test
python test for OmniPro by Damian Dzik

## Running the app
Assuming that we have python installed on our machine.

Open the terminal and navigate to the folder that the app is in.
Once we get to the folder with the app we can type in the command:

``` terminal
    python app.py
```

In Visual Studio Code (VSC).

Click on the app.py file in the explorer. then click he play button that is in the top right hand corner of the screen.

These two methods should work and run the app.

## Description

This is a console app. It can be ran by following the steps above.

This app allows the user to:
- display information of a car by id
- get the average price of a car by make
- get the average price of a car by model

### Firstly
We display a menu for hte user to chose from 3 different options. 
```
          ----------------------------
          | Menu                     
          ----------------------------
          | 1. List car info by id        
          | 2. Average price of car  
          ----------------------------
          | 0. Exit                  
          ----------------------------
```
- option 1) list car info by id
- option 2) Average price of car
- option -) Exit

### List car info by id Option 1)
The function responsible for this functionality is called carById() and it takes in a parameter of int which is the id of the car.
```python
        # checking for inputs
        if userInput == 1:
            try:
                carid = int(input("Please enter id of car to get: "))
            except ValueError:
                print("Value is not a number, Please try again.")
                continue
            carById(carid)
```
This function then uses the passed in id of the car to iterate through the cars in the cars json.

We use a for loop to iterate through the list
```python
    for car in data['cars']:
```
Then we check if the id of the current car object matches with the passed in id. 
- if the id's match we display all information except chassis_no and we break out of the loop
- If they don't then we display an error message

### Average price of car Option 2)
This option has two functions.
- get average price of car by make
- get average price of car by model
  
These two functions are very similar therefore I will explain only one of them.

When the user choses option 2. A sub menu will be displayed asking the user to chose yet again an option from another two options.

```
          -------------------------------
          | Get average price by:       
          -------------------------------
          | 1. Make                     
          | 2. Model                    
          -------------------------------
```
Lets say the user choses to get average price of a car by make.

Another sub menu will be displayed with all of the makes of cars that exist in the cars json.
The for loop below is responsible displaying car make info in the menu.
```python
for x in finalList:
        menuString += "| {}) {} \n          ".format(str(finalList.index(x)),x)
```
This means that if a new car of a different make is added to the json. The app will automatically ad it to the sub menu without coding it yourself. This is particularly handy as we do not have to do anything ourselves except adding a new car to the cars json.

The user can enter the index of the make that they want to get the average price for.

Then we use the index of the make the user entered to count how many cars of that make are in the cars json.

After that we are going to get the accumulated price of all the cars of that make. We use a for loop to iterate through the cars and ge their prices if the cars are of the chosen make.
```python
    accumPrice = 0
    for car in data['cars']:
        if car['make'] == make:
            accumPrice += car['price']
```
We can finally calculate and print the average price of cars of x make.
```python
    avgPrice = int(accumPrice / count)
    print("The average price of {} is: {}".format(make, avgPrice))  
```

# Structure
We have one main function that is responsible for the whole app. In this function we call all of the other functions and display menus. Doing it this way makes it easy to read and navigate through. It has a clear nice flow.

I tried to build the app in a way that would allow us to add more cars into the cars json and not have to worry about having to refactor any code. Therefore the sub menus where we print information about the car models and makes, we use a for loop to iterate through the necessary information and get rid of any duplicates.

### Link
Here is the link to the public repository on my GitHub page: [repo](https://github.com/ddzik19/python-test)

