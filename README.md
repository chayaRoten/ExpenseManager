## Welcome to Our Project!

### Project Overview

Our goal is to provide a seamless backend infrastructure for the "Balance" application, allowing users to handle their expenses and income effortlessly. While backend development is our primary focus, frontend development will be handled by our frontend team.

### System Specification

- **Database:** MongoDB will manage our data efficiently.
- **Server-side:** We're using Python for server-side development.
- **Client-side:** React will power our client-side interface.

### Application Features

- **User Routes:** Includes registration, login, and profile update functionalities.
- **Expense and Income Routes:** Supports creation, update, deletion, and retrieval of expense and income data.
- **Visualization Route:** Allows users to extract data suitable for visualization using matplotlib.

### Quality Assurance

We're committed to delivering a high-quality product. Our developers will write comprehensive tests to ensure the system's performance meets our standards.

### Documentation

Quality documentation is crucial for maintaining transparency and ensuring future scalability. Detailed documentation, including design specifications and usage guidelines, can be found in the `docs` directory.

### Thank You!

Thank you for your dedication to this project. We look forward to creating something amazing together!

### Tree

├── app\
│   ├── models\
│   │  ├── budget_management.py\
│   │  └── user.py\
│   ├── routes\
│   │  ├── budget_management_router.py\
│   │  ├── user_router.py\
│   │  └── visualiztion_router.py\
│   ├── services\
│   │  ├── budget_management_CRUD.py\
│   │  ├── db.py\
│   │  ├── user_CRUD.py\
│   │  └── visualiztion.py\
│   ├── log.py\
│   └── main.py\
├── requirements.txt\
├── tests\
│   ├── budget_management_test.py\
│   └── users_test.py\
└──  README.md\




## Table of Contents

- [About](#about)
- [Usage](#usage)
- [Routes](#routes)

## About <a name = "about"></a>

A Basic Project for final Python Project

### Installing

Download this package, and then run:

```
pip install fastApi
```

and the server side runs!


## Usage <a name = "usage"></a>

Server Base URI:  <b>http://127.0.0.1:8000 </b>
Use this Basic url with the correct route listed below

see Api:     <b>http://127.0.0.1:8000/docs </b>



### Available routes <a name = "routes"></a>

### User Routes
#### Get user  



#### Login  

```http
  POST /user/login
```  
Response: User Object

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `id`                  |  user id the user entered at login |
| `username`            |  user name the user entered at login |
| `password`            | user password the user entered at login |

#### Sign Up - create User  

```http
  POST /user/signUp
``` 
Response: User Object 

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `user`                |  full user object with all parameters, includes username, id and password|

#### Update User

```http
  PUT /user
``` 
Response: User Object 

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `user`                |  full user object with all parameters, includes username, , id and password|
 id of the service|

### Budget Management Routes

#### Get Budget Management of users

```http
  GET /budget?userId={user_id}
```

Response: object of Budget Management

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `user_id`                | id of the user to get budget management - send as query params!|

#### Create Budget Management

```http
  POST /budget
```

Response: addBudget

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `revenues`                | amount of revenue|
| `expenses`                | amount of expenses|
| `userId`                | id of the user|

#### Update Budget Management

```http
  PUT /budget
```

Response: updateBudget

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `Budget Management`             | full Budget Management object |

#### Delete Budget Management

```http
  DELETE /budget
```

| Parameter             |  Description                  |
| :----------------     |  :-------------------------   |
| `id`                | id of the user|

Response: deleteBudget
