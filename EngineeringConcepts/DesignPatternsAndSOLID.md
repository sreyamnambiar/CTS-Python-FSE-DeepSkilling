# Design Patterns and SOLID Principles

## Introduction

Design Principles and Design Patterns are fundamental concepts in software engineering. They help developers write clean, maintainable, reusable, and scalable code.

The SOLID principles are a set of design guidelines for Object-Oriented Programming (OOP), while Design Patterns are proven solutions to commonly occurring software design problems.

---

# SOLID Principles

## 1. Single Responsibility Principle (SRP)

### Definition

A class should have only one responsibility and one reason to change.

### Real-Life Example

In a school:

* Teacher teaches students.
* Accountant manages fees.

Each person has only one responsibility.

### Python Example

```python
class Student:
    def __init__(self, name):
        self.name = name

class StudentRepository:
    def save(self, student):
        print(f"Saving {student.name}")

class EmailService:
    def send_email(self, student):
        print(f"Sending email to {student.name}")
```

### Benefits

* Easier maintenance
* Better readability
* Reduced complexity

---

## 2. Open Closed Principle (OCP)

### Definition

Software entities should be open for extension but closed for modification.

### Real-Life Example

A smartphone allows installing new applications without changing the operating system.

### Python Example

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def area(self):
        return 3.14 * 5 * 5

class Rectangle(Shape):
    def area(self):
        return 10 * 20
```

New shapes can be added without modifying existing code.

### Benefits

* Easy feature additions
* Reduced risk of bugs

---

## 3. Liskov Substitution Principle (LSP)

### Definition

Objects of a derived class should be able to replace objects of the base class without affecting program correctness.

### Real-Life Example

A Car can replace a Vehicle because it behaves like a Vehicle.

### Python Example

```python
class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    pass

vehicle = Car()
vehicle.move()
```

### Benefits

* Proper inheritance hierarchy
* Predictable behavior

---

## 4. Interface Segregation Principle (ISP)

### Definition

Clients should not be forced to depend on methods they do not use.

### Real-Life Example

A Robot can work but does not eat.

### Python Example

```python
class Workable:
    def work(self):
        pass

class Eatable:
    def eat(self):
        pass

class Human(Workable, Eatable):
    pass

class Robot(Workable):
    pass
```

### Benefits

* Smaller interfaces
* Better flexibility

---

## 5. Dependency Inversion Principle (DIP)

### Definition

High-level modules should depend on abstractions, not concrete implementations.

### Real-Life Example

A USB-C charger can work with different devices.

### Python Example

```python
class Database:
    def connect(self):
        pass

class MySQL(Database):
    def connect(self):
        print("Connected to MySQL")

class Application:
    def __init__(self, db):
        self.db = db

db = MySQL()
app = Application(db)
```

### Benefits

* Loose coupling
* Easier testing and maintenance

---

# Design Patterns

## What are Design Patterns?

Design Patterns are reusable solutions to commonly occurring software design problems.

They are generally categorized into:

* Creational Patterns
* Structural Patterns
* Behavioral Patterns

---

# 1. Singleton Pattern

## Definition

Ensures that only one instance of a class exists.

## Real-Life Example

A school has only one Principal.

## Python Example

```python
class Singleton:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)
```

### Output

```text
True
```

## Use Cases

* Database Connections
* Logger
* Configuration Manager

---

# 2. Factory Pattern

## Definition

Provides an interface for creating objects without exposing object creation logic.

## Real-Life Example

A restaurant kitchen prepares food based on the customer's order.

## Python Example

```python
class Car:
    def drive(self):
        print("Driving Car")

class Bike:
    def drive(self):
        print("Riding Bike")

class VehicleFactory:

    @staticmethod
    def create_vehicle(vehicle_type):

        if vehicle_type == "car":
            return Car()

        return Bike()

vehicle = VehicleFactory.create_vehicle("car")
vehicle.drive()
```

## Use Cases

* Vehicle Creation
* Payment Gateways
* UI Components

---

# 3. Builder Pattern

## Definition

Constructs complex objects step-by-step.

## Real-Life Example

Building a custom burger with selected ingredients.

## Python Example

```python
class Burger:

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

burger = Burger()

burger.add_item("Bun")
burger.add_item("Patty")
burger.add_item("Cheese")

print(burger.items)
```

### Output

```text
['Bun', 'Patty', 'Cheese']
```

## Use Cases

* Report Generation
* User Profiles
* Configuration Objects

---

# 4. Observer Pattern

## Definition

Defines a one-to-many dependency between objects.

## Real-Life Example

YouTube subscribers receive notifications whenever a creator uploads a new video.

## Python Example

```python
class Subscriber:

    def update(self, message):
        print(message)

class Channel:

    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)

channel = Channel()

user = Subscriber()

channel.subscribe(user)

channel.notify("New video uploaded!")
```

## Use Cases

* Notifications
* Event Systems
* Stock Market Updates

---

# 5. Strategy Pattern

## Definition

Allows selecting an algorithm dynamically at runtime.

## Real-Life Example

Google Maps can provide:

* Car route
* Bike route
* Walking route

## Python Example

```python
class CarStrategy:

    def travel(self):
        print("Travel by Car")

class BikeStrategy:

    def travel(self):
        print("Travel by Bike")

class Navigator:

    def __init__(self, strategy):
        self.strategy = strategy

    def navigate(self):
        self.strategy.travel()

navigator = Navigator(CarStrategy())

navigator.navigate()
```

## Use Cases

* Payment Methods
* Sorting Algorithms
* Route Selection


