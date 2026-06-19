"""============================================================

HANDS-ON 1 : Web Framework Foundations & Django Project Setup

============================================================

------------------------------------------------------------

1. Request-Response Cycle

------------------------------------------------------------

Example Request:

GET /api/courses/

Flow:

Browser

↓

URL Router (urls.py)

↓

View (views.py)

↓

Model (models.py) -> Database Query

↓

View Processes Data

↓

HttpResponse / Template Response

↓

Browser

Description:

When a user sends a request, Django first checks the URL

patterns. The matching view function is executed. The view

may communicate with the model to fetch or update data in

the database. The view then returns a response which is sent

back to the browser.

------------------------------------------------------------

2. Middleware

------------------------------------------------------------

Middleware sits between the request and the view, and also

between the view and the response.

Flow:

Request

↓

Middleware

↓

View

↓

Middleware

↓

Response

Built-in Middleware Examples:

1. SessionMiddleware

Manages user sessions and stores session data across requests.

2. AuthenticationMiddleware

Identifies the currently logged-in user and attaches user

information to the request object.

------------------------------------------------------------

3. WSGI vs ASGI

------------------------------------------------------------

WSGI = Web Server Gateway Interface

ASGI = Asynchronous Server Gateway Interface

WSGI:

- Traditional Python web standard

- Handles requests synchronously

- Suitable for normal web applications

ASGI:

- Modern asynchronous interface

- Supports concurrent connections

- Supports WebSockets, real-time applications,

live chat systems and notifications

Django uses WSGI by default.

We switch to ASGI when:

- Building real-time applications

- Using WebSockets

- Handling many concurrent connections

- Developing asynchronous applications

------------------------------------------------------------

4. MVC and Django MVT

------------------------------------------------------------

MVC = Model View Controller

Model:

Handles data and database operations.

View:

Handles the user interface.

Controller:

Handles application logic and user requests.

Django follows MVT = Model View Template

Model:

Handles data and database operations.

View:

Contains business logic and processes requests.

Template:

Handles presentation and user interface.

MVC to Django MVT Mapping

MVC Model      -> Django Model

MVC View       -> Django Template

MVC Controller -> Django View

------------------------------------------------------------

5. Django Project Files

------------------------------------------------------------

settings.py

Contains project configuration such as installed apps,

database settings, middleware and security settings.

urls.py

Maps URLs to view functions.

wsgi.py

Entry point for WSGI-compatible web servers.

asgi.py

Entry point for ASGI-compatible web servers.

------------------------------------------------------------

6. Django Project vs Django App

------------------------------------------------------------

Django Project:

The complete web application configuration.

A project can contain multiple apps.

Example:

coursemanager

Django App:

A self-contained module that provides a specific feature.

Example:

courses

Project Structure Example:

coursemanager (Project)

│

├── courses (App)

├── students (App)

├── faculty (App)

└── library (App)

Therefore:

Project = Entire Application

App = Individual Feature/Module"""
