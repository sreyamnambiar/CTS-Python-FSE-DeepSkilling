# Hands-On 3 - Django REST Views, URL Routing & Forms

## What this handson covers
This handson explains how to build REST APIs in Django using Django REST Framework (DRF), how to connect serializers and views, how to set up URL routing, and how to use ViewSets and Routers.

## Main concepts
- DRF: a toolkit for building APIs in Django.
- REST API: a way for applications to communicate using HTTP and JSON.
- Serializer: converts Django model data into JSON and validates incoming JSON.
- APIView: a class-based view for writing GET, POST, PUT, and DELETE manually.
- ViewSet: a class that groups common API actions together.
- Router: automatically creates URLs for ViewSets.
- Request: data sent from client to server.
- Response: data sent back from server to client.
- Status codes: HTTP codes like 200, 201, 204, 400, and 404.


- courses/serializers.py
- courses/views.py
- courses/urls.py
- coursemanager/urls.py
- coursemanager/settings.py

## Commands to run
1. pip install djangorestframework
2. python manage.py check
3. python manage.py runserver

## API endpoints
- GET /api/course-list/
- POST /api/course-list/
- GET /api/course-detail/<id>/
- PUT /api/course-detail/<id>/
- DELETE /api/course-detail/<id>/
- GET /api/courses/<id>/students/


