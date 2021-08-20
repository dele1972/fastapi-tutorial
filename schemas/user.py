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