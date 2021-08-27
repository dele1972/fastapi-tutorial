# FastAPI MongoDB REST API in Python | CRUD Operations | Swagger | PyMongo

Source (YouTube): [FastAPI MongoDB REST API in Python | CRUD Operations | Swagger | PyMongo](https://youtu.be/G7hZlOLhhMY) by Mahesh Kariya (16.05.2021)

- See on GitHub too: [itsmaheshkariya/fastapi-mongodb-restapi](https://github.com/itsmaheshkariya/fastapi-mongodb-restapi)

## 1 - Python

Python3 is preinstalled on Ubuntu 20.04

## 2 - pip(3)

I use pip3 instead. Maybe a Link will follow.

## 3 - Virtual venv

I use virtualenvwrapper. Maybe a Link will follow.

## 4 - pip3 install needed packages (fastapi pymongo uvicorn)

```bash
pip3 install fastapi pymongo uvicorn
```

| Package                                      | Description                                                                         |
|----------------------------------------------|-------------------------------------------------------------------------------------|
| [FastAPI](https://fastapi.tiangolo.com/)     | framework, high performance, easy to learn, fast to code, ready for production      |
| [pymongo](https://pypi.org/project/pymongo/) | tools for interacting with MongoDB database from Python                             |
|                                              | (native Python driver for MongoDB)                                                  |
| [Uvicorn](https://www.uvicorn.org/)          | Uvicorn is a lightning-fast ASGI server implementation, using uvloop and httptools. |
|                                              | [ASGI](https://asgi.readthedocs.io/en/latest/)                                      |
|                                              | (Asynchronous Server Gateway Interface)                                             |
|                                              | is a spiritual successor to WSGI, intended to provide a standard interface          |
|                                              | between async-capable Python web servers, frameworks and applications.              |

## 5 - Install MongoDB

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | \
  sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
sudo apt-get update -y
sudo apt-get install -y mongodb-org
```

- **some infos**:
  - data directory: `/var/lib/mongodb`
  - log directory:  `/var/log/mongodb`
  - user account: `mongodb`
  - configuration file: `/etc/mongod.conf`
  - **start**: `sudo systemctl start mongod`
      - on failure: `sudo systemctl daemon-reload`
  - **status**: `sudo systemctl status mongod`
  - **stop**: `sudo systemctl stop mongod`
  - restart: `sudo systemctl restart mongod`
  - start session: `mongosh`
  - Link: [Install MongoDB Community Edition on Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

## 6 - Install MongoDB client from VS Store in VS Code

## Tutorial

Create a project folder:
```bash
mkdir ~/dev/tutorial    # his ~/Desktop/py-mongo
codium ~/dev/tutorial
```

Create a folder for the MongoDB database and start it:
```bash
mkdir ~/dev/tutorial/data
mongod --dbpath=data
sudo systemctl stop mongod
```

Optional: Install mongoDB Extension for VS Codium and connect to database:

- VS Codium
  - Extension: `MongoDB for VS Code`
  - connect with connection string: `mongodb://localhost:27017`

mongodb data lost if mongodb is killed and restartet without any arguments

### Start working

1. **Start virtualenv**: `workon tutorial`
  - or create it: `mkvirtualenv tutorial`
  - for validation: `workon`
2. **Start MongoDB**: `sudo systemctl start mongod`
3. **Start Backend**: `uvicorn index:app --reload`

### Stop working

1. **Stop Backend**: ctrl + c
2. **Stop MongoDB**: `sudo systemctl stop mongod`
3. **Stop virtualenv**: `deactivate`

### Links offered by FastAPI

| Link                        | Description                                                          |
| --------------------------- | -------------------------------------------------------------------- |
| http://127.0.0.1:8000/      | API root                                                             |
| http://127.0.0.1:8000/docs  | [Swagger UI](https://swagger.io/tools/swagger-ui/) API Documentation |
| http://127.0.0.1:8000/redoc | [ReDoc](https://redoc.ly/redoc) API Documentation                    |
