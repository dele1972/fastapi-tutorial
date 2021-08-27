# convert from python model (model/user.py:User) to mongoDB document
def userEntity(item) -> dict:
    return{
        "id": str(item["_id"]),
        "name": item["name"],
        "email": item["email"],
        "password": item["password"]
    }

# define a list of users
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

# Here follows a less specific alternative 
# - otherwise you would have to define a model for each DB schema as above

# instead of `userEntity`
def serializeDict(a) -> dict:
    return {
        **{i: str(a[i]) for i in a if i == '_id'},
        **{i: str(a[i]) for i in a if i != '_id'}
    }

# instead of `usersEntity`
def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]