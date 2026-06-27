from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CourseDetailView, CourseListView, CourseViewSet, EnrollmentViewSet, StudentViewSet


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')

urlpatterns = [
    path('course-list/', CourseListView.as_view(), name='course-list'),
    path('course-detail/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('', include(router.urls)),
]
