import pymongo


def get_dbconn():
    client = pymongo.MongoClient(
        "mongodb+srv://epsilonites-20:NCR%40Hack2021@epsilonites-20.1dkev.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    )

    db = client["cfreps"]
    return db