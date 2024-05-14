# pythonfinalproject

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
