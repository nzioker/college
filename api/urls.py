from django.urls import path
from .views import all_students, student, add_student

urlpatterns = [
    path('all-students', all_students, name='students'),
    path('student/<int:pk>', student, name='student'),
    path('add-student/', add_student, name='add-student'),
]