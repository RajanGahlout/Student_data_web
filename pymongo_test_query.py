# importing module

from pymongo import MongoClient
import ssl

import pprint


# creation of MongoClient

client = MongoClient()



# Connect with the portnumber and host


client = MongoClient("mongodb+srv://Rajangahlout:Capg12345@cluster0.p6ksttg.mongodb.net/?retryWrites=true&w=majority")


db = client.javatpoint

employee = {"id": "100",

            "stname": "Ashu",

            "age": "18",
            "course": "btech",

            "email": "abc@gmail.com",

            }

# Creating document

employees = db.employees

# Inserting data

#employees.insert_one(employee)

# Fetching data

pprint.pprint(employees.find_one())

