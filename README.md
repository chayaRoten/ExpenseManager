# Expense Manager Backend

This project provides a backend infrastructure for managing expenses and income, developed using Python and FastAPI. The application supports user authentication, expense tracking, and data visualization.

## Project Overview

- **Database:** MongoDB for data storage.
- **Server-side:** Developed using Python and FastAPI.
- **Visualization:** Data can be visualized using Matplotlib.

## Application Features

- **User Routes:** Handles user registration, login, and profile updates.
- **Expense and Income Routes:** Supports creation, update, deletion, and retrieval of expense and income data.
- **Visualization Route:** Extracts data for visualization with Matplotlib.

## Quality Assurance

Comprehensive tests are included to ensure the system's performance and reliability. Logs and documentation are maintained for transparency and future scalability.

## Installation

To get started, clone this repository and install the required packages:

```bash
pip install fastapi[all] pymongo matplotlib
```

## Running the Server

Run the FastAPI server with the following command:

```bash
uvicorn main:app --reload
```

Access the server at [http://127.0.0.1:8000](http://127.0.0.1:8000). For API documentation, visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Available Routes

### User Routes

#### Login

```http
POST /user/login
```

Response: User Object

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `id`        | User ID entered at login                 |
| `username`  | Username entered at login                |
| `password`  | Password entered at login                |

#### Sign Up - Create User

```http
POST /user/signUp
```

Response: User Object

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `user`      | Full user object with all parameters     |

#### Update User

```http
PUT /user
```

Response: User Object

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `user`      | Full user object with all parameters     |

### Budget Management Routes

#### Get Budget Management

```http
GET /budget?userId={user_id}
```

Response: Budget Management Object

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `user_id`   | ID of the user for budget management     |

#### Create Budget Management

```http
POST /budget
```

Response: Budget Management Object

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `revenues`  | Amount of revenue                        |
| `expenses`  | Amount of expenses                       |
| `userId`    | ID of the user                           |

#### Update Budget Management

```http
PUT /budget
```

Response: Updated Budget Management Object

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `budget`    | Full Budget Management object            |

#### Delete Budget Management

```http
DELETE /budget
```

Response: Deleted Budget Management Object

| Parameter   | Description                              |
|-------------|------------------------------------------|
| `id`        | ID of the budget to delete               |


### Project Tree

```
├── app
│   ├── models
│   │   ├── budget_management.py
│   │   └── user.py
│   ├── routes
│   │   ├── budget_management_router.py
│   │   ├── user_router.py
│   │   └── visualization_router.py
│   ├── services
│   │   ├── budget_management_CRUD.py
│   │   ├── db.py
│   │   ├── user_CRUD.py
│   │   └── visualization.py
│   ├── log.py
│   └── main.py
├── requirements.txt
├── tests
│   ├── budget_management_test.py
│   └── users_test.py
└── README.md
```


