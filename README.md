# Llevame
Carpooling app for the final project in Holberton School

# Deploy development or production
To deploy a development or production environment, (after installing docker) follow the next steps:
- clone this repository.
- Inside the cloned repository run:
    - docker build -t python:llevame .
    - docker-compose up --no-start
    - docker-compose start

# API Guide

## “/api/users"

### GET
#### Return a list with all users
- Response is a JSON with the next information **id, first_name, last_name, type_id, n_document,  department, city, picture, email, is_driver and date_joined**

**Example**

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "first_name": "Victor Armando",
            "last_name": "Arteaga Fernandez",
            "type_id": "CC",
            "n_document": "1234",
            "department": 3,
            "city": 3,
            "picture": "http://localhost:8000/media/pictures/MockupWeb_2.png",
            "email": "vic@gmail.com",
            "is_driver": "True",
            "date_joined": "2020-06-11T02:48:43.532600Z"
        }
    ]
}
```

### POST

#### Create a new user
- Body fields required: **first_name, last_name, type_id, n_document, department, city, email, password and password2**
- Fields not required: **picture**

**Example**
```json
{
    "body": {
		'first_name': 'Juan',
		'last_name': 'Buitrago',
		'type_id': 'CC',
		'n_document': '1145779861121',
		'department': '1',
		'city': '1',
		'password': '123',
		'password2': '123',
		'email': 'test@gmail.com'
	}
}
```

- Response is a JSON with the next information: **id, first_name, last_name, type_id, n_document,  department, city, picture, email, is_driver and date_joined**

```json
{
    "response": "User created successfully",
    "user": {
        "id": 10,
        "first_name": "Juan",
        "last_name": "Buitrago",
        "type_id": "CC",
        "n_document": "1145779861121",
        "department": 1,
        "city": 1,
        "picture": null,
        "email": "test@gmail.com",
        "is_driver": "True",
        "date_joined": "2020-06-14T04:33:19.366373Z"
    }
}
```

##  "/api/users/user_id"

### GET
#### Return User information by ID
- Response is a JSON with the next information **id, first_name, last_name, type_id, n_document,  department, city, picture, email and date_joined**

**Example**

```json
{
    "id": 2,
    "first_name": "Victor Armando",
    "last_name": "Arteaga Fernandez",
    "type_id": "CC",
    "n_document": "1234",
    "department": 3,
    "city": 3,
    "picture": "http://localhost:8000/media/pictures/MockupWeb_2.png",
    "email": "vic@gmail.com",
    "is_driver": "True",
    "date_joined": "2020-06-11T02:48:43.532600Z"
}
```

### PUT
#### Update user information
- Body fields that can be send, each one is optional:  **first_name, last_name, department, city, picture and is_driver**
- Require Token to be Authenticated

**Example**

```json
{
	"body": {
			'first_name': 'Andres',
			'last_name': 'Arteaga',
			'department': '1',
			'city': '1',
			'picture': '('picture', open('/path/to/file','rb'))',
            "is_driver": "True",
		}
	'headers': {
			'Authorization': 'Token 290ba582e34cad353272038a4203993943f8c1fc'
		}
}
```

- Response is a JSON with the next information **id, first_name, last_name, type_id, n_document,  department, city, picture, email, is_driver and date_joined**

**Example**

```json
{
    "response": "Successfully updated",
    "user": {
        "id": 2,
        "first_name": "Andres",
        "last_name": "Arteaga",
        "type_id": "CC",
        "n_document": "1234",
        "department": 1,
        "city": 1,
        "picture": null,
        "email": "vic@gmail.com",
        "is_driver": "True"
        "date_joined": "2020-06-11T02:48:43.532600Z"
    }
}
```

## “/api/departments"

### GET
#### Returns a list of all departments
- Response is a JSON with the next information: **id, name and code**

**Example**

```json
{
    "count": 33,
    "next": "http://localhost:8000/api/departments/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "name": "Antioquia",
            "code": 5
        },
        {
            "id": 2,
            "name": "Atlantico",
            "code": 8
        },
        {
            "id": 3,
            "name": "D. C. Santa Fe de Bogotá",
            "code": 11
        }, ...
    ]
}
```

## “/api/cities"

### GET
#### Returns a list of all cities
- Response is a JSON with the next information: **id, department_id, code and name**

**Example**

```json
{
    "count": 1126,
    "next": "http://localhost:8000/api/cities/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "department": 1,
            "code": 1,
            "name": "MEDELLIN"
        },
        {
            "id": 2,
            "department": 1,
            "code": 2,
            "name": "ABEJORRAL"
        },
        {
            "id": 3,
            "department": 1,
            "code": 4,
            "name": "ABRIAQUI"
        }, ...
    ]
}
```

## "/api/departments/department_id/cities"

### GET
#### Returns a list of all cities from a department
- Response is a JSON with the next information: **id, department_id, code and name**

**Example**

```json
[
    {
        "id": 125,
        "department": 1,
        "code": 895,
        "name": "ZARAGOZA"
    },
    {
        "id": 124,
        "department": 1,
        "code": 893,
        "name": "YONDO"
    },
    {
        "id": 123,
        "department": 1,
        "code": 890,
        "name": "YOLOMBO"
    }, ...
]
```

## "/api/login"

### POST
#### Log a user with email and password
- Body required fields: **Email and password**

**Example**

```json
{
		"body": {
			'username': 'vic@gmail.com',
			'password': '123'}
}
```

- Response is a JSON with the next information: **Token and  user_id**

**Example**

```json
{
    "token": "290ba582e34cad353272038a4203993943f8c1fc",
    "user_id": 2
}
```