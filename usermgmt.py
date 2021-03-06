import redis
from fastapi import FastAPI

app = FastAPI()
r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

@app.get("/")
def home():
    return {"welcome":"home"}

@app.get("/createuser/{name}/{descript}")
def createUser(name:str, descript:str):
    username = "user" + str(str(r.scan().count("user")))
    r.hset(username, "name", name)
    r.hset(username, "desc", descript)
    return username

@app.get("/allusers")
def getAllUsers():
    users = {}
    for i in r.keys():
        users [i] = {"name":r.hget(i, "name"), "description":r.hget(i, "desc")}
    return users

@app.get("/getuser/{userID}")
def getSingleUser(userID:str):
    user = {
        "name":r.hget(userID, "name"), 
        "description":r.hget(userID, "desc")   
    }
    return user