import pymongo
import os

MONGODB_URI = "mongodb+srv://root:azurecollin123@cluster0.spljg.mongodb.net/?retryWrites=true&w=majority"

DBS_NAME = "myFirstdb"
COLLECTION_NAME = "myFirstTable"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


# conn = mongo_connect(MONGODB_URI)
# coll = conn[DBS_NAME][COLLECTION_NAME]

# documents = coll.find().limit(5)

# for doc in documents:
#     print(doc)\

def show_menu():
    print("")
    print("1. Add a Record")
    print("2. Find a Record")
    print("3. Edit a Record")
    print("4. Delete a Record")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def add_record():
    print("")
    first = input("Enter first name > ")
    last = input("Enter last name > ")
    dob = input("Enter Date of Birth (dd/mm/yyyy) > ")
    gender = input("Enter gender (m/f) > ")
    hair_colour = input("Enter hair colour > ")
    occupation = input("Enter occupation > ")
    nationality = input("Enter nationality > ")

    new_doc = {'first': first, 'last': last, 'dob': dob, 'gender': gender,
               'hair_colour': hair_colour, 'occupation': occupation, 'nationality': nationality}

    try:
        coll.insertOne(new_doc)
        print("")
        print("Doc inserted")
    except:
        print("Error connecting to Database")

def get_record():
    print("")
    first = input("Enter First Name > ")
    last = input("Enter Last Name > ")

    try:
        doc = coll.find_one({"first": first, "last": last})
    except:
        print("Error")
    if not doc:
        print("Error No Results Found")
    return doc

def find_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k + ": " + v)


def edit_record():
    doc = get_record()
    if doc:
        print("")
        for k,v in doc.items():
            if k != "_id":
                print(k + ": " + v)
    print("")
    userInput = input("Enter which field you want to edit > ")
    if userInput == "first":
        print("")
        firstNew = input("Enter NEW First Name > ")
        try: 
            coll.update_one(doc, {'$set': {'first': firstNew}})
        except:
            print("Error")
    elif userInput == "last":
        print("")
        lastNew = input("Enter NEW Last Name > ")
        try: 
            coll.update_one(doc, {'$set': {'last': lastNew}})
        except:
            print("Error")
    elif userInput == "dob":
        print("")
        dobNew = input("Enter NEW Date of Birth (dd/mm/yyyy) > ")
        try: 
            coll.update_one(doc, {'$set': {'dob': dobNew}})
        except:
            print("Error")
    elif userInput == "gender":
        print("")
        genderNew = input("Enter NEW Gender (m/f) > ")
        try: 
            coll.update_one(doc, {'$set': {'gender': genderNew}})
        except:
            print("Error")
    elif userInput == "hair_colour":
        print("")
        hairNew = input("Enter NEW Hair Colour > ")
        try: 
            coll.update_one(doc, {'$set': {'hair_colour': hairNew}})
        except:
            print("Error")
    elif userInput == "occupation":
        print("")
        occupNew = input("Enter NEW Occupation > ")
        try: 
            coll.update_one(doc, {'$set': {'occupation': occupNew}})
        except:
            print("Error")
    elif userInput == "nationality":
        print("")
        nationalityNew = input("Enter NEW Nationality > ")
        try: 
            coll.update_one(doc, {'$set': {'nationality': nationalityNew}})
        except:
            print("Error")
    else:
        print("Wrong Field!")

def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            print("Delete Record")
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid Option!")




conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()


# mongodb+srv://root:<azurecollin123>@cluster0.spljg.mongodb.net/?retryWrites=true&w=majority


# Update the first matching Record
# Match: nationality: 'irish'
# set the hair colour: 'purple
##SINGLE##
# coll.update({first: 'eve', last: 'ryan'}, {$set:{hair_colour: 'purple'}});
##MULTI##
# coll.updateMany({nationality: "irish"}, {$set:{hair_colour: 'purple'}});
# coll.update({nationality: "irish"}, {$set:{hair_colour: 'purple'}},{multi:true})

# Delete a record that has a first of kate and last of bush????

# Delete martha fenton
## coll.deleteOne({first: "martha", last: "fenton"});
## coll.remove({first: "martha", last: "fenton"});
