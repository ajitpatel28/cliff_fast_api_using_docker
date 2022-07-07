# User authentication using FastAPI (a python frameworks), Docker Compose (for deployment)
## How to start the application


**The commands:**

First you have to git clone the files by entering in your terminal:
```
$ git clone https://github.com/AtamanKit/fastapi_users_docker.git
```  
Then start the application:
```
$ docker-compose up -d
```
The above command will both create the images and start the containers ( images and  container for the FastAPI application).

For visualizing the application, open up your browser and enter:

* http://127.0.0.1:8000/docs

In the application we have seven sections:
* For authentication (the right green "Authorize" button from the above);
* For creating tokens for new users (Enter details in user/signup );
* For creating tokens by entering user's credentials;
* For watching the current user (only if authenticated);
* For modifying user properties (only if authenticated with admin role);
* For deleting the user.

To see the runing containers in docker, enter in the terminal:
```
$ docker ps
```
To see the database and collection created (database name is: myTestDB, collection: users) enter in your terminal:
```
$ docker exec -it <container-id> bash
```

## Configuration and file structure
Our file structure is:
```
.
├── app
│   ├── Dockerfile
│   ├── __init__.py
│   ├── main.py
│   ├── requirements.txt
│   ├── index.py
│   ├── models.py
│   ├── auth_bearrer.py
│   ├── auth_handller.py
└── docker-compose.yml
```
In the app directory  file I made all the files .

```models.py``` file is the one that containes all the needed pydantic models (models.py), database and authentication variables are define in ```auth_handller.py``` and ```bearrer.py```. 

Authentication is made by using ```bearer``` scheme with ```token``` creation and usage.


