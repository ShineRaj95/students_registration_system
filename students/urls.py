from django.urls import path
from . import views

""" Urlpatterns array maps routes to definitions defined in views.py.
path function is used to map a url string to a view. The url striing is 
given as the first argument of the path function, the second argument
is the view function the url string should point to and the third argument
specifies the name of the route. The url string segment enclosed by angle
brackets reprsent variables and these are passed to the view function as
arguments
"""
urlpatterns = [
    path('',views.student_listing_page,name='list-students'),
    path('create/',views.add_students,name='add-student'),
    path('edit-student/<int:student_id>',views.edit_students,name='edit-student'),
    path('delete-student/',views.delete_student,name='delete-student'),
    path('filtered-students/',views.filter_students,name='filtered-student'),
    path('filtered-students-by-course/',views.filter_students_by_course,name='filtered-student-by-course'),
    path('logout',views.logout_view,name='auth-logout'),

]