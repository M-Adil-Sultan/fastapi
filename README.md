
# FastApi Example Project

FastApi Project Structure

## Project Structure

```bash
fastapi/
├── app/
│   ├── api/
│   │   ├── controllers/
│   │   │   ├── product_controller.py
│   │   │   ├── cart_controller.py
│   │   │   ├── order_controller.py
│   │   │   ├── auth_controller.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── models/
│   │   ├── product.py
│   │   ├── cart.py
│   │   ├── order.py
│   │   ├── user.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── product_service.py
│   │   ├── cart_service.py
│   │   ├── order_service.py
│   │   ├── auth_service.py
│   │   └── __init__.py
│   ├── utils/
│   │   ├── security.py
│   │   └── __init__.py
│   ├── database/
│   │   ├── connection.py
│   │   └── __init__.py
│   ├── dependencies/
│   │   ├── auth.py
│   │   └── __init__.py
│   ├── routes/
│   │   ├── product_routes.py
│   │   ├── cart_routes.py
│   │   ├── order_routes.py
│   │   ├── auth_routes.py
│   │   └── __init__.py
│   ├── main.py
│   └── settings.py
├── tests/
│   ├── test_product.py
│   ├── test_cart.py
│   ├── test_order.py
│   ├── test_auth.py
│   └── __init__.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```


- **app**: The main application package.
-    **api**: Contains API-related code and endpoints.
-    **controllers**: Individual API Controllers (endpoints) are defined here.
-    **models**: Contains data models or Pydantic models.
-    **services**: Houses business logic or service layer components.
-    **utils**: Contains utility functions or helper modules.
-    **database**: Handles database-related code, such as database connection and schemas.
-    **dependencies**: Contains dependencies or dependency providers.
-    **main.py**: Entry point of the application.
-    **routes/api.py**: Base Routes Configuration.
-    **settings.py**: Configuration settings for the application.
-    **tests**: Contains test modules and test cases.
-    **.env**: Environment variables for the project.
-    **.gitignore**: Specifies the files and directories to be ignored by Git.
-    **requirements.txt**: List of project dependencies.


## Run Locally

Clone the project

```bash
  git clone https://github.com/M-Adil-Sultan/fastapi.git
```

Go to the project directory

```bash
  cd fastapi
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

or This Command in Windows

```bash
  python -m uvicorn main:app --reload
```


