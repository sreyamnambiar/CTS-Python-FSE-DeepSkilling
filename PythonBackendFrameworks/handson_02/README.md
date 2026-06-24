# Cognizant Digital Nurture 5.0 - Python FSE Hands-On 2

## Django Models, ORM, and Admin Interface



### 1. Models in `courses/models.py`

```python
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_dept = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return f"{self.code} - {self.name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='students')
    enrollment_year = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        unique_together = [['student', 'course']]

    def __str__(self):
        return f"{self.student} - {self.course}"
```

### 2. Admin in `courses/admin.py`

```python
from django.contrib import admin

from .models import Course, Department, Enrollment, Student


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credits', 'department')
    search_fields = ('name', 'code', 'department__name')
    list_filter = ('department', 'credits')


admin.site.register(Department)
admin.site.register(Student)
admin.site.register(Enrollment)
```

### 3. What Each Field Type Does

- `CharField`: stores short text such as names, codes, and labels.
- `IntegerField`: stores whole numbers such as credits and years.
- `DecimalField`: stores exact decimal values such as budgets and money-related values.
- `EmailField`: stores email addresses and validates the email format.
- `DateField`: stores a date value without time.
- `ForeignKey`: creates a relationship where many records can point to one parent record.

### 4. Core Concepts

- **Model**: a Python class that maps to a database table.
- **Migration**: a Django file that describes database schema changes.
- **ForeignKey**: a relationship field that links one model to another.
- **ORM**: Object-Relational Mapping, Django's way of working with the database using Python objects instead of raw SQL.
- **unique_together**: a constraint that keeps a combination of fields unique across rows.

### 5. Migration Commands

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py showmigrations
```

- `makemigrations`: creates migration files from model changes.
- `migrate`: applies migrations to the database.
- `showmigrations`: displays all migrations and shows which ones have been applied.

### 6. Django Shell Data Creation

Run these commands inside `python manage.py shell`:

```python
from courses.models import Department, Course, Student

cs = Department.objects.create(
    name="Computer Science",
    head_of_dept="Dr. Sharma",
    budget=500000.00
)

ece = Department.objects.create(
    name="Electronics",
    head_of_dept="Dr. Rao",
    budget=400000.00
)

course1 = Course.objects.create(name="Python Programming", code="CS101", credits=4, department=cs)
course2 = Course.objects.create(name="Database Systems", code="CS102", credits=3, department=cs)
course3 = Course.objects.create(name="Digital Logic", code="ECE101", credits=4, department=ece)
course4 = Course.objects.create(name="Microprocessors", code="ECE102", credits=3, department=ece)

student1 = Student.objects.create(first_name="Aarav", last_name="Mehta", email="aarav@example.com", department=cs, enrollment_year=2023)
student2 = Student.objects.create(first_name="Isha", last_name="Patel", email="isha@example.com", department=cs, enrollment_year=2022)
student3 = Student.objects.create(first_name="Rohan", last_name="Verma", email="rohan@example.com", department=ece, enrollment_year=2023)
student4 = Student.objects.create(first_name="Neha", last_name="Singh", email="neha@example.com", department=ece, enrollment_year=2021)
student5 = Student.objects.create(first_name="Kabir", last_name="Joshi", email="kabir@example.com", department=cs, enrollment_year=2024)
```

### 7. ORM Queries

Fetch all courses in Computer Science department:

```python
Course.objects.filter(department__name="Computer Science")
```

Count courses per department using `annotate()`:

```python
from django.db.models import Count

Department.objects.annotate(course_count=Count("courses")).values("name", "course_count")
```

Fetch students with departments using `select_related()`:

```python
Student.objects.select_related("department").all()
```

Increase department budget by 10% using `F()`:

```python
from django.db.models import F

Department.objects.filter(name="Computer Science").update(budget=F("budget") * 1.10)
```

### 8. Superuser and Admin Panel

Create a superuser:

```bash
python manage.py createsuperuser
```

Start the development server:

```bash
python manage.py runserver
```

Open the admin panel in the browser:

```text
http://127.0.0.1:8000/admin/
```

Log in with the superuser credentials to access the admin interface and manage Department, Course, Student, and Enrollment records.
