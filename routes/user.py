from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()

# db = local
# collection = user

@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(usersEntity(conn.local.user.find()))
    return usersEntity(conn.local.user.find())

# @param user acceppts model/user.py:User 
@user.post('/')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return usersEntity(conn.local.user.find())