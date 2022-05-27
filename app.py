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
        "chasis_no":"12345A",
        "id":1,
        "last_updated":"2017-02-01 00:00:00",
        "price":500.0
    },{
        "make":"Nissan",
        "model":"Micra",
        "year":2004,
        "chasis_no":"12425A",
        "id":6,
        "last_updated":" 2017-03-01 00:00:00",
        "price":400.0
    },{
        "make":"Ford",
        "model":"Fiesta",
        "year":2002,
        "chasis_no":"12345B",
        "id":2,
        "last_updated":" 2017-03-01 00:00:00",
        "price":300.0
    },{
        "make":"Audi",
        "model":"A3",
        "year":"",
        "chasis_no":"12345C",
        "id":3,
        "last_updated":" 2017-04-01 00:00:00",
        "price":0
    },{
        "make":"Nissan",
        "model":"Micra",
        "year":"2004",
        "chasis_no":"12345D",
        "id":4,
        "last_updated":" 2017-05-01 00:00:00",
        "price":200.0
    },{
        "make":"Peugot",
        "model":"308",
        "year":"1998",
        "chasis_no":"12345E",
        "id":5,
        "last_updated":" 2017-06-01 00:00:00",
        "price":100.0
    }]
    }
    """

# we turn the json string to json obj
data = json.loads(cars)

# testing if the json database works
for car in data['cars']:
    print(car['id'])