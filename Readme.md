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

Open `http://localhost:8000` in your browser to see the Web UI of this
project.


```
http://localhost:8000/
```

Screenshots of Web UI:

![1](https://user-images.githubusercontent.com/80194170/177830239-b33b1a37-0e58-4655-a77b-4816ae5ac251.png)

![UI_2](https://user-images.githubusercontent.com/80194170/177830202-24eda5b9-4dc6-4a32-a38b-e08bfab62c86.png)


##Screenshots of API responses using Curl:

1.user/login

![userlogin](https://user-images.githubusercontent.com/80194170/177830679-439d1788-e9c1-4c0b-aa8a-6b4864a60c1a.png)

2.user/signup:

![usersignup](https://user-images.githubusercontent.com/80194170/177830604-3c0c26a9-4573-4fc5-80b3-16f20dbbde64.png)

3.Count_brands_by_products:

![count_brands_by_products](https://user-images.githubusercontent.com/80194170/177829872-c4bb4f94-6776-4535-93a4-4f07f60a17a9.png)

4.count_discounted_products:

![count_discounted_products](https://user-images.githubusercontent.com/80194170/177830787-01a8f409-6f57-454e-b483-ce71e375dc2f.png)

5.count_high_offer_price:

![count_high_offer_price](https://user-images.githubusercontent.com/80194170/177830881-a0bfe64b-245b-44bb-890f-7b399d550b5c.png)

6.count_high_discount_products_brand:

![high_discount_products_brand](https://user-images.githubusercontent.com/80194170/177831092-03e45340-338e-4170-a204-a929455b0836.png)

7.top_20_discounting_brands:

![high_discount_products_brand](https://user-images.githubusercontent.com/80194170/177831142-571b8ae4-99fa-45a2-8b8f-bf7c83f61fda.png)

8.count_by_category_and_stock:

![count_by_category_stock](https://user-images.githubusercontent.com/80194170/177831231-7cb51d15-59f1-46fa-8ef9-9529aeb28fd6.png)




