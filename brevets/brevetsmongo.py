from pymongo import MongoClient
import os

client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)
db = client.mydb

# Use collection "lists" in the databse
collection = db.lists

def insert_brevet(brevet_dist, start_time, control_list):
    """
    Inserts a new brevet data into the database

    Inputs a Dist(int), time(str) and a control_list (list of dictionaties
    Returns the unique ID assigned to the document by mongo (primary key.)
    """
    output = collection.insert_one({
        "brevet_dist": brevet_dist,
        "start_time": start_time,
        "control_list": control_list})
    _id = output.inserted_id  # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)
def retrieve_brevet():
    """
    Obtains the newest document in the "Control_List" collection in database "brevetsdb".
    Returns dist (int), time(str) and Control_List(list of dictionaries) as a tuple.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    controls_listed = collection.find().sort("_id", -1).limit(1)

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for controls in controls_listed:
        return controls["brevet_dist"], controls["start_time"], controls["control_list"]