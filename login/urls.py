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
    path('',views.login,name='auth-login'),
]