from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path("courses/", views.courses, name="courses"),
    path('courses/details/<int:id>', views.details, name='course_details'),
]
